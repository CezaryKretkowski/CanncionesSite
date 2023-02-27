from django.db import models

class OrderList(models.Model):
    order=models.ForeignKey('Order', related_name='OrderList', on_delete=models.CASCADE)
    user=models.ForeignKey('User', related_name='OrderList', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.order)
    
    def getOrder(self):
        return self.order