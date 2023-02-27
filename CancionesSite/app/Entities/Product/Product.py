from django.urls import reverse
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..Dictionary.ProductDetails.Brand import Brand
from ..Dictionary.SubCategory import SubCategory
from .Customization import Customization

class Product(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    brand = models.ForeignKey(Brand, related_name='Product', on_delete=models.CASCADE)
    subCategory = models.ForeignKey(SubCategory, related_name='Product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    description = models.TextField(max_length=1000)
    rating = models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(1)])
    available = models.BooleanField(default=True)
    specialOffer = models.BooleanField(default=False)
    specialPrice = models.DecimalField(max_digits=12, decimal_places=2,null=True)
    customization = models.ForeignKey(Customization, related_name='Product', on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='images/')
    
    def get_absolute_url(self):
        return reverse("app:ProductDetails", args=[str(self.id)])
    
    def add_To_Cart(self):
        return reverse("app:Cart/add", args=[str(self.id)])
    
    def Customization(self):
        return reverse("app:Customization", args=[str(self.id)])
    
    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'app_product'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'