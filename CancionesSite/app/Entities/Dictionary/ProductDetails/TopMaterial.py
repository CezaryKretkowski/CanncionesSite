from django.db import models

class TopMaterial(models.Model):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    class Meta:
        verbose_name = 'TopMaterial'
        verbose_name_plural = 'TopMaterials'

    def __str__(self):
        return str(self.name)