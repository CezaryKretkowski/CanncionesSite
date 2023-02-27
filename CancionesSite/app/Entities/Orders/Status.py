from django.db import models

class Status(models.Model):
    type = models.CharField(max_length=255)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return str(self.type)