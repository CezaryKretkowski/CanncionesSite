from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Citis'

    def __str__(self):
        return str(self.name)