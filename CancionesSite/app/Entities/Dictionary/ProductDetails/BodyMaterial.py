from django.db import models

class BodyMaterial(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    class Meta:
        verbose_name = 'BodyMaterial'
        verbose_name_plural = 'BodyMaterials'

    def __str__(self):
        return str(self.name)
