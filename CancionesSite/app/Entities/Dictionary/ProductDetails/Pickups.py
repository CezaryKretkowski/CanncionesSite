from django.db import models

class Pickups(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()
    
    class Meta:
        verbose_name = 'Pickups'
        verbose_name_plural = 'Pickups'

    def __str__(self):
        return str(self.name)