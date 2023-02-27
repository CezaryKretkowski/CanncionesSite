from django.conf import settings
from decimal import Decimal
from .Entities.Product.Product import Product
from uuid import uuid4,UUID
import copy

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        
        
        
        try: 
            products=Product.objects.filter(id__in=product_ids)
        except Product.DoesNotExist:
            products=[]
                            
        cart = copy.deepcopy(self.cart)
        for product in products:
            cart[str(product.id)]['product'] = product
            

        for item in cart.values():
            item['total_price'] = item['price'] * item['quantity']
            yield item
        
        
    def getProductFromBasket(self,uuid):        
        try:
            product=Product.objects.get(id=uuid)
        except:
            product=None

        return product;  
                 
    def add(self, product, quantity):
        
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()
        
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def delete(self, product_id):

        if product_id in self.cart:
            
            del self.cart[product_id]
            self.session.modified = True
            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())  
    
    def update(self, product_id, qty):
        product_id=str(product_id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = int(qty)
        self.save()
        
    def save(self):
        self.session.modified = True