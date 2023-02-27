from django.shortcuts import render
from .Entities.Dictionary.Category import Category
from .Views.Products.SubCategoryView import SubCategoryView


def home(request):
    category = ['Gitary/basy', 'Akcesoria', ]
    return render(request, 'store/Home.html')


def getMainCategory(request):
    try:
        data=Category.objects.all()
    except Category.DoesNotExist:
        data=[]
        
    return {'mainCategory': data}


def register(request):
    return render(request, 'store/Register.html')


def login(request):
    return render(request, 'store/Login.html')
