from django.utils import timezone
from uuid import uuid4
from django.db import models
from .Status import Status
from ..Users.Address import Address

class Order(models.Model):
    name = models.CharField(max_length=300)
    lastName = models.CharField(max_length=300)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=12)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    addres = models.ForeignKey(Address, related_name='Order', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name='Order', on_delete=models.CASCADE,default=1)
    order_place_date=models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    
    
    class Meta:
        verbose_name =  'Order'
        verbose_name_plural =  'Orders'

    def __str__(self):
        return str(self.id);
