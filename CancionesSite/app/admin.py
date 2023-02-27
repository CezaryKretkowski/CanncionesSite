from django.contrib import admin
from .Entities.Dictionary.Category import Category
from .Entities.Dictionary.SubCategory import SubCategory
from .Entities.Dictionary.ProductDetails.Brand import Brand
from .Entities.Product.Product import Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',  'image']
    # prepopulated_fields = {'slug': ('name',)}
    list_editable = ['name',  'image']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',  'category', 'image']
    # prepopulated_fields = {'slug': ('name',)}
    list_editable = ['name',  'image']
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']

@admin.register(Product)    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name',  'brand', 'subCategory','price','description','rating','available'
                    ,'specialOffer','specialPrice','image']
  
    list_editable = ['name', 'brand', 'subCategory','price','description','rating','available'
                    ,'specialOffer','specialPrice']