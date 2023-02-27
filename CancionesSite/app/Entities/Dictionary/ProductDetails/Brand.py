from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return str(self.name)