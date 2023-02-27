from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ..Login.Login import Login
import uuid 
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.shortcuts import render
from ...Views.Registration.Registration import RegistrationForm
from ...Entities.Users.User import User
from ...Entities.Users.Address import Address
from ...Entities.Users.OrderList import OrderList
from ...Entities.Orders.Order import Order
from ...Entities.Orders.ProductList import ProductList
from ...Entities.Product.Product import Product
from django.db import connection
from ...Entities.Product.Rating import Rating

class UserView(LoginRequiredMixin,View):
    login_url="/login"
    redirect_field_name="redirected_to"
    user = None
    def getRegForm(self,user):
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
            'username':str(user.user_name),
            'email':str(user.email), 
            'first_name':str(user.first_name), 
            'last_name':str(user.last_name),
            'password':'',
            'confirmPassword':'',
            'street':street,
            'zipcode':zip_code,
            'number':number,
            'flat_number':flatNumber
        }
        return RegistrationForm(intaial_data)    
        
    def get(self, request, **kwargs):
        user=request.user
        ordersAndProducts=[]
        try:
            orders=OrderList.objects.filter(user=user)
            productsIDS=Rating.objects.filter(user=user).values_list('product')
            UserproductsIDS=ProductList.objects.filter(order__in=orders.values_list('order')).exclude(product__in=productsIDS).values_list("product")
            Userproducts=Product.objects.filter(id__in=UserproductsIDS).distinct()
            for i  in orders:
                print(ProductList.objects.filter(order=i.order))
                ordersAndProducts.append( {"order":i.order,"product":ProductList.objects.filter(order=i.order)})            
        except User.DoesNotExist:
             print('BrakZamówien')
             orders=[]
             Userproducts=[]
                    
        regForm=self.getRegForm(user=user)       
        if isinstance(user,AnonymousUser):
            return HttpResponseRedirect("/login")
        else:
            return render(request,"store/UserView.html",{"user":user,"regForm":regForm,'OrderList':ordersAndProducts,"Userproducts":Userproducts})
        
        
    def post(self, request, **kwargs):
        user=request.user
        ordersAndProducts=[]
        
        if "rate" in request.POST:
            
            try:
                product=Product.objects.get(id=request.POST['rate'])
            except Product.DoesNotExist:
                return HttpResponseRedirect("/userview")
            Rating.objects.create(user=user,product=product,rate=request.POST['rating'],comment=request.POST['comment'])
            return HttpResponseRedirect("/userview")
        
        try:
            orders=OrderList.objects.filter(user=user)
            productsIDS=Rating.objects.filter(user=user).values_list('product')
            UserproductsIDS=ProductList.objects.filter(order__in=orders.values_list('order')).exclude(product__in=productsIDS).values_list("product")
            Userproducts=Product.objects.filter(id__in=UserproductsIDS).distinct()
            for i  in orders:
                print(ProductList.objects.filter(order=i.order))
                ordersAndProducts.append( {"order":i.order,"product":ProductList.objects.filter(order=i.order)})            
        except User.DoesNotExist:
             print('BrakZamówien')
             orders=[]
             Userproducts=[]
        
        
               
        regForm=RegistrationForm(request.POST)
        if 'password' in request.POST:
            password=request.POST['password']
            user.set_password(password)
            user.save()
            
        if 'settings' in request.POST:
            if regForm.is_valid():
                user.username=regForm.cleaned_data['username']
                user.email=regForm.cleaned_data['email']
                user.user=regForm.cleaned_data['first_name']
                user.last_name=regForm.cleaned_data['last_name']
                user.address.street=regForm.cleaned_data['street']
                user.address.number=regForm.cleaned_data['number']
                user.address.flat_number=regForm.cleaned_data['flat_number']
                user.save()
                
        if isinstance(user,AnonymousUser):
            return HttpResponseRedirect("/login")
        else:
            return render(request,"store/UserView.html",{"user":user,"regForm":regForm,'OrderList':ordersAndProducts,"Userproducts":Userproducts})
