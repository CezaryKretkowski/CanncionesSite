from django.views import View
from django.shortcuts import render
from ...Entities.Product.Product import Product
from ...Entities.Dictionary.SubCategory import SubCategory
from ...Entities.Dictionary.ProductDetails.Brand import Brand
from django.http import HttpResponseRedirect
from ...Cart import Cart
from .OrderForm import OrderForm
from django.contrib.auth.models import AnonymousUser
from ...Entities.Users.Address import Address
from ...Entities.Dictionary.Address.City import City
from ...Entities.Users.OrderList import OrderList
from django.db import connection
from ...Entities.Orders.Order import Order
from ...Entities.Orders.Status import Status
from django.http import HttpResponse
from ...Entities.Orders.ProductList import ProductList
from ...Entities.Product.Rating import Rating
class ProductDetails(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        
        try:
            product=Product.objects.get(id=pk)
            cart = Cart(request)
        except Product.DoesNotExist:
            product=None
        # for p in products:
        #     if p.uuid == uid:
        #         self.product = p   
                
                
        print(product.subCategory.category.id)
        if isinstance(request.user,AnonymousUser)==False:
            user=request.user
            
            address=user.address
            
            if address:
                street=str(address.street)
                zip_code=str(address.zipCode)
                number=str(address.number)
                flatNumber=str(address.flatNumber)
            else:
                street=""
                zip_code=""
                flatNumber=""
                number=""
            intaial_data = {
                'email':str(user.email), 
                'first_name':str(user.first_name), 
                'last_name':str(user.last_name),
                'street':street,
                'zipcode':zip_code,
                'number':number,
                'flat_number':flatNumber
            }
            ordeForm=OrderForm(initial=intaial_data)
        else:
            ordeForm=OrderForm()
        
        
        try:
            rateList=Rating.objects.filter(product=product)
        except:
            rateList=[]
        
        try:
            cities = City.objects.all()
        except City.DoesNotExist:
            cities=[]
                
            
        return render(request,"store/ProductDetails.html",{"product":product,"cart":cart,"cities":cities,'orderForm':ordeForm,"rating":rateList})

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']  
        cart=Cart(request)     
        try:
            product=Product.objects.get(id=pk)
        except Product.DoesNotExist:
            product=None
        # for p in products:
        #     if p.uuid == uid:
        #         self.product = p 
        if 'addToCart' in request.POST:
            qt= request.POST['qt']
            cart.add(product,int(qt))
            return HttpResponseRedirect('/Cart')
        
        cart = Cart(request)
        ordeForm=OrderForm(request.POST)
        try:
            cities = City.objects.all()
        except City.DoesNotExist:
            cities=[]
            
        try:
            rateList=Rating.objects.filter(product=product)
        except:
            rateList=[]
        
        if "placeOrder" in request.POST:
            if ordeForm.is_valid():
                clenData=ordeForm.cleaned_data
                cityID=request.POST['city']
                try:
                    city=City.objects.get(id=cityID)
                except City.DoesNotExist:
                    return HttpResponse("error")
                print("placeOrder")  
                try:
                    status=Status.objects.get(id=1)
                except Status.DoesNotExist:
                    return HttpResponse("error")
                addres=Address.objects.create(street=clenData['street'],number=clenData['number'],
                                           zipCode=clenData['zipcode'],
                                           flatNumber=clenData['flat_number'],
                                           city=city)
                
                order=Order.objects.create(name=clenData['first_name'],lastName=clenData['last_name'],email=clenData['email'],phoneNumber=request.POST['phone']
                                           ,price=cart.get_total_price(),addres=addres,status=status)
                print(request.POST)
                
                        
                ProductList.objects.create(order=order,product=self.product,qunatitii=1)                     
                            
                print('problem1')       
                if isinstance(request.user,AnonymousUser)==False:
                    OrderList.objects.create(order=order,user=request.user)
                return render(request,"store/Order.html")
                    
        return render(request,"store/ProductDetails.html",{"product":self.product,"cart":cart,"cities":cities,'orderForm':ordeForm,"rating":rateList})