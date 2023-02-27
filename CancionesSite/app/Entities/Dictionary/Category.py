from django.urls import reverse
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    image = models.ImageField(upload_to='images/Category/')
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse("app:SubCategoryView", args=[str(self.id)])
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
