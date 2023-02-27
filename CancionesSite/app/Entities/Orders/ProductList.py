from django.db import models
from ..Product.Product import Product
from .Order import Order

class ProductList(models.Model):
    order=models.ForeignKey(Order, related_name='ProductList', on_delete=models.PROTECT,db_constraint=False)
    product=models.ForeignKey(Product, related_name='ProductList', on_delete=models.CASCADE)
    qunatitii=models.IntegerField()
    objects = models.Manager()

        
    def __str__(self):
        return str(self.product)
        
    def getProduct(self):
        try:
            return self.product
        except Product.DoesNotExist:
            return None;