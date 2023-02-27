from django.db import models
from ..Users.User import User
from .Product import Product
from django.core.validators import MaxValueValidator, MinValueValidator


class Rating(models.Model):
    user = models.ForeignKey(User, related_name='Rating', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='Rating', on_delete=models.CASCADE)
    rate = models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(1)]);
    comment = models.TextField(max_length=1000,null=True)
    
    def __str__(self):
        return str(self.name)

