from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from ...Entities.Product.Customization import Customization
from django import forms
from django.forms.widgets import TextInput
import uuid
from ...Entities.Product.Product import Product
from ...Entities.Orders.Order import Order
from ...Entities.Orders.Status import Status
from django.contrib.auth.models import AnonymousUser
from ...Entities.Users.Address import Address
from ...Entities.Dictionary.Address.City import City
from ...Entities.Users.OrderList import OrderList
from ...Entities.Orders.ProductList import ProductList
from django.http import HttpResponse
from .OrderForm import OrderForm

class CustomizationForm(forms.ModelForm):
    
    class Meta:
        model = Customization
        fields = ['color','topMaterial','bodyMaterial','pickups']
        widgets = {
             'color':TextInput(attrs={'class':'form-control'}),
        }
            
class CustomizationView(View):
    def get(self, request, **kwargs):
        form=CustomizationForm()
        uid = kwargs['pk']
        
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
            product=Product.objects.get(id=uid)
        except Product.DoesNotExist:
            product=None
            
        try:
            cities = City.objects.all()
        except City.DoesNotExist:
            cities=[]
        
        return render(request,"store/Custumization.html",{"Form":form,"product":product,"cities":cities,'orderForm':ordeForm,})
    
    def post(self, request, **kwargs):
        uid = kwargs['pk']
        ordeForm=OrderForm(request.POST)
        try:
            product=Product.objects.get(id=uid)
        except Product.DoesNotExist:
            product=None
        if 'addToCart' in request.POST:
            form=CustomizationForm(request.POST)
            if form.is_valid():
                p=form.save()
                w=product
                w.pk=None
                w.customization=p
                w.save()
                return HttpResponseRedirect(w.add_To_Cart()) 
            else:
                print(form.errors)
                
        if "placeOrder" in request.POST:
            if ordeForm.is_valid():
                form=CustomizationForm(request.POST)
                print(request.POST)
                p=Customization.objects.create(color=request.POST['color'],topMaterial_id=request.POST['topMaterial'],bodyMaterial_id=request.POST['bodyMaterial'],pickups=request.POST['pickups'])
                w=product
                w.pk=None
                w.customization=p
                w.save()
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
                                           ,price=product.price,addres=addres,status=status)
                print(request.POST)
                
                        
                ProductList.objects.create(order=order,product=w,qunatitii=1)                     
                            
                print('problem1')       
                if isinstance(request.user,AnonymousUser)==False:
                    OrderList.objects.create(order=order,user=request.user)
                    
            return render(request,"store/Order.html")