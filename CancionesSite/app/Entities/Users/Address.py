from uuid import uuid4
from django.db import models
from django.core.validators import  MinValueValidator
from ...Entities.Dictionary.Address.City import City

class Address(models.Model):
    street = models.CharField(max_length=255)
    number = models.IntegerField(default=1,validators=[MinValueValidator(1)])
    zipCode = models.CharField(max_length=6)
    flatNumber = models.IntegerField(default=1,validators=[MinValueValidator(1)])
    city = models.ForeignKey('City', related_name='Address', on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'


        
    def __str__(self):
        return str(self.street) +" "+ str(self.number)+"/"+str(self.flatNumber)+" zip-code "+str(self.zipCode) 