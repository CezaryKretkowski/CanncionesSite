from django.urls import reverse
from django.db import models


class SubCategory(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    category = models.ForeignKey(
        'Category', related_name='SubCategory', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/Category/SubCategory/')
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse("app:ProductList", args=[str(self.id)])
    class Meta:
        verbose_name_plural = 'SubCategories'

    def __str__(self):
        return self.name
