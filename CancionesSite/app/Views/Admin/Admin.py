import uuid
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django_staff_required.views import StaffRequiredMixin
from ...Entities.Product.Product import Product
from ...Entities.Orders.Order import Order
from ...Entities.Users.User import User
from ...Entities.Orders.ProductList import ProductList
from ...Entities.Orders.Status import Status
from django import forms
from django.core.mail import send_mail
import random
import string

class ProdouctForm(forms.ModelForm):
    class Meta:
        model = Product 

        fields = ['name','brand','subCategory','price','description','available'
                  ,'rating','specialOffer','specialPrice','image']

class OrderForm(forms.ModelForm):
    class  Meta:
        model = Order
        fields = ['status']

class AdminView(StaffRequiredMixin,View):
    login_url="/login"
    redirect_field_name="redirected_to"
    user = None
    
    
    def get(self, request, **kwargs):
        productForm=ProdouctForm()
        products=Product.objects.all()
        orders=Order.objects.all()
        ordersAndProducts=[]
        
        users=User.objects.all()
        try:
            for i  in orders: 
                w=0;                  
                ordersAndProducts.append( {"order":i,"form":OrderForm(initial={'status':i.status}),"product":ProductList.objects.filter(order=i)})
                w=w+1 
        except:
            pass
        return render(request,"store/Admin.html",{"ProductsForm":productForm,"productsList":products,"Orders":ordersAndProducts,'Users':users})
    
    def post(self, request, **kwargs):
        productForm=ProdouctForm()
        products=Product.objects.all()
        orders=Order.objects.all()
        ordersAndProducts=[]
        EditId=None
        users=User.objects.all()
        try:
            w=0;
            for i  in orders:                   
                ordersAndProducts.append( {"order":i,"form":OrderForm(initial={'status':i.status}),"product":ProductList.objects.filter(order=i)}) 
                w=w+1        
        except:
            pass
        
        if "save_orderStatus" in request.POST:
            try:
                order=orders=Order.objects.get(id=request.POST['save_orderStatus'])
                order.status=Status.objects.get(id=request.POST['status'])
                order.save()
                mesage="Hai "+str(order.name) + " your status order was changed \nOrder: "+ str(order.id)+ " status:"+str(order.status)
                # send_mail(subject="Change Order Status",
                #           message=mesage,
                #           from_email="cancionessiteproject@gmail.com",
                #           recipient_list=[order.email]
                #           )
                
                
            except Order.DoesNotExist:
                pass
            
            
        if "resetPassword" in request.POST:
            try:
                user=User.objects.get(id=request.POST['resetPassword'])
                password=""
                for i in range(8): 
                    password=password+random.choice(string.ascii_letters)
                user.set_password(password)
                user.save()
                mesage="Hai "+str(user.first_name) + " your Password has been reset \nYour new Password: "+ str(password)+ " \n\nPlease for safty reason change your password"
                # send_mail(subject="Change Password",
                #           message=mesage,
                #           from_email="cancionessiteproject@gmail.com",
                #           recipient_list=[user.email]
                #           )
            except User.DoesNotExist:
                pass
     
        if "blockUser" in request.POST:
            try:
                user=User.objects.get(id=request.POST['blockUser'])
                password=""
                for i in range(8): 
                    password=password+random.choice(string.ascii_letters)
                user.set_password(password)
                user.save()
                mesage="Hai "+str(user.first_name) + " your account has been block to unblock your account pless contact admintrator!!!"
                # send_mail(subject="Block Account",
                #           message=mesage,
                #           from_email="cancionessiteproject@gmail.com",
                #           recipient_list=[user.email]
                #           )
            except User.DoesNotExist:
                pass
        if 'edit' in request.POST:
            data=request.POST['edit']
            # product = next((product for  product in Product.objects.all() if product.uuid==uuid.UUID(data)),None)
            try:
                product=Product.objects.get(id=request.POST['edit'])
            except Product.DoesNotExist:
                product = None
            
            intaial_data = {
                'name':product.name, 
                'brand':product.brand,
                'subCategory':product.subCategory,
                'price':product.price,
                'description':product.description,
                'rating':product.rating,
                'specialOffer':product.specialOffer,
                'specialPrice':product.specialPrice,
                'image':product.image.url
            }
            EditId=product.id
            productForm=ProdouctForm(initial=intaial_data)
        else:
            productForm=ProdouctForm()
        if "addProduct" in request.POST:
            productForm=ProdouctForm(request.POST,request.FILES)
            if productForm.is_valid():
                productForm.save()
            else: 
                print(productForm.errors)
                # data=productForm.cleaned_data
                # Product.objects.create(name=data['name'],brand=data['brand'],subCategory=data['subCategory'],price=data['price']
                #                        ,description=data['description']
                #                        ,rating=data['rating']
                #                        ,available=data['available']
                #                        ,specialOffer=data['specialOffer']
                #                        ,specialPrice=data['specialPrice']
                #                        ,customization=None
                #                        ,image=data['image'])
            
        if "editProduct" in request.POST:
            product=Product.objects.get(id=request.POST['editProduct'])
            productForm=ProdouctForm(request.POST,request.FILES,instance=product)
            if productForm.is_valid():
                productForm.save()
            
            print(productForm.errors)
            # print(request.POST)
            # data=request.POST
            # p
            # product.name=data['name']
            # product.brand_id=data['brand']
            # product.subCategory_id=data['subCategory']
            # product.price=data['price']
            # product.description=data['description']
            # product.rating=data['rating']
            
            # product.image=data['image']
            # product.save()
           
        users=User.objects.all()    
        orders=Order.objects.all() 
            
        forms=[{"order":i,"form":OrderForm(initial={'status':i.status})}for i in orders]
            
        return render(request,"store/Admin.html",{"ProductsForm":productForm,"productsList":products,"Orders":ordersAndProducts,'Users':users,"EditID":EditId}) 
       