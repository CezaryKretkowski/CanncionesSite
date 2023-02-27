from uuid import uuid4
from django.db import models
from ..Dictionary.ProductDetails.BodyMaterial import BodyMaterial
from ..Dictionary.ProductDetails.TopMaterial import TopMaterial
from ..Dictionary.ProductDetails.Pickups import Pickups

class Customization(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    color = models.CharField(max_length=7,default="#FFFFFF")
    topMaterial = models.ForeignKey(TopMaterial, related_name='Customization', on_delete=models.CASCADE,null=True)
    bodyMaterial = models.ForeignKey(BodyMaterial, related_name='Customization', on_delete=models.CASCADE,null=True)
    pickups = models.ForeignKey(Pickups, related_name='Customization', on_delete=models.CASCADE,null=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Customizations'

    def __str__(self):
        return str(self.color)