from django.views import View
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from ...Entities.Dictionary.Category import Category
from ...Entities.Dictionary.SubCategory import SubCategory
from ...Utilities.Utilities import Utilities

class SubCategoryView(View):
    def get(self, request, *args, **kwargs):
        pk=kwargs['pk']
        print(pk)
        try :
            category=Category.objects.all().filter(pk=pk)  
            categories=Category.objects.all()
        except Category.DoesNotExist:
            category=[]
            categories=[]
        try:       
             subCategorys=SubCategory.objects.all().filter(category=category[0])
             subCateg0=SubCategory.objects.all()
        except SubCategory.DoesNotExist: 
            print("faild1")
            subCategorys=[]
            subCateg0=[]
        
        subCat=Utilities().chanks(subCategorys,3)
        print(subCat)
        return render(request,"store/SubCategory.html",{"subCategories":subCat,"categoryName":category[0].name,"subCat":subCateg0
                                                        ,"Categories":categories})

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')