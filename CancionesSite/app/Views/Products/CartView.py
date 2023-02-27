from django.views import View
from django.shortcuts import render
from ...Entities.Product.Product import Product
from ...Entities.Dictionary.SubCategory import SubCategory
from ...Entities.Dictionary.ProductDetails.Brand import Brand
from ...Entities.Dictionary.Address.City import City
from .OrderForm import OrderForm
from ...Cart import Cart
from  django.http import HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser
from ...Entities.Users.Address import Address
from ...Entities.Orders.Order import Order
from ...Entities.Orders.Status import Status
from django.http import HttpResponse
from ...Entities.Orders.ProductList import ProductList
from ...Entities.Users.OrderList import OrderList



class CartView(View):
    

        
    def add_To_Card(request,pk):
        print(pk)
        cart=Cart(request)
        try:
            product=Product.objects.get(id=pk)
            
        except Product.DoesNotExist:
            product=None
        if product != None:
            product=cart.add(product,1)
            

        return HttpResponseRedirect('/Cart/')
    
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
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
            cities = City.objects.all()
        except City.DoesNotExist:
            cities=[]
            
        
        
        return render(request,"store/Cart.html",{"cart":cart,"cities":cities,'orderForm':ordeForm})
    
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        ordeForm=OrderForm(request.POST)
        try:
            cities = City.objects.all()
        except City.DoesNotExist:
            cities=[]
        
        if "placeOrder" in request.POST:
            if ordeForm.is_valid():
                clenData=ordeForm.cleaned_data
                cityID=request.POST['city']
                try:
                    city=City.objects.get(id=cityID)
                except City.DoesNotExist:
                    return HttpResponse("error city")
                
                try:
                    status=Status.objects.get(id=1)
                except Status.DoesNotExist:
                    return HttpResponse("error id")
                addres=Address.objects.create(street=clenData['street'],number=clenData['number'],
                                           zipCode=clenData['zipcode'],
                                           flatNumber=clenData['flat_number'],
                                           city=city)
                
                order=Order.objects.create(name=clenData['first_name'],lastName=clenData['last_name'],email=clenData['email'],phoneNumber=request.POST['phone']
                                           ,price=cart.get_total_price(),addres=addres,status=status)
                
                for i in cart: 
                    cart.delete(product_id= str(i['product'].id))   
                    ProductList.objects.create(order=order,product=i['product'],qunatitii=i['quantity']) 
                    # for j in range(i['quantity']): 
                        
                        # with connection.cursor() as cursor:
                        #     cursor.execute("Insert INTO app_productlist (order_id,productRef_id) values('"+str(order.id)+"','"+str(i['product'].uuid)+"');")                      
                            
                    
                if isinstance(request.user,AnonymousUser)==False:
                    OrderList.objects.create(order=order,user=request.user)
                return render(request,"store/Order.html")
                
        
        if "delete-button" in request.POST:
            cart.delete(product_id= str(request.POST.get('delete-button')))
            
        if "productid" in request.POST:
            cart.update(product_id=request.POST['productid'],qty=request.POST['productqty'])
        
        return render(request,"store/Cart.html",{"cart":cart,"cities":cities,'orderForm':ordeForm})