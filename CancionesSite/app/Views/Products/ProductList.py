from django.views import View
from django.shortcuts import render
from ...Entities.Product.Product import Product
from ...Entities.Dictionary.SubCategory import SubCategory
from ...Entities.Dictionary.ProductDetails.Brand import Brand
from django.db.models import Avg, Max, Min
from django.db.models import FloatField



class ProductList(View):
    
    def orderProduct(self,orderID,product):
        if orderID == '1':            
            return product.order_by('price')            
        elif orderID == '2':
            
            return product.order_by('-price')
        elif orderID == '3':
            
            return product.order_by('rating')
        elif orderID == '4':
            
            return product.order_by('name')
        elif orderID == '5':
            
            return product.order_by('-name')
        else:
            
            return product
            
            
    
    def get(self, request, *args, **kwargs):
        pk=kwargs['pk']
        try:
            product=Product.objects.filter(subCategory=pk,customization = None)
            maxNum=product.aggregate(Max('price', output_field=FloatField())).get('price__max')
            productName=SubCategory.objects.filter(id=pk)
        except Product.DoesNotExist:
            product=[]
            productName=[]
            maxNum=0
        brands=product.values('brand').distinct()
        try:
            brands=Brand.objects.filter(id__in=brands)
        except Brand.DoesNotExist:
            brands=[]
             
        return render(request,"store/ProductList.html",{"products":product,"ProductName":productName[0].name,"brands":brands,"selectItem":0,"maxPrice":maxNum,
                                                         "brandsFiter":[],"selectedRate":"1","specOffer":0})

    def post(self, request, *args, **kwargs):
         
        pk=kwargs['pk']
        try:
            product=Product.objects.filter(subCategory=pk,customization = None)
            maxNum=product.aggregate(Max('price', output_field=FloatField())).get('price__max')
            productName=SubCategory.objects.filter(id=pk)
        except Product.DoesNotExist:
            product=[]
            productName=[]
            maxNum=0
        brands=product.values('brand').distinct()
        try:
            brands=Brand.objects.filter(id__in=brands)
        except Brand.DoesNotExist:
            brands=[]
        
        
        if 'sort' in request.POST:
            products=self.orderProduct(request.POST['sort'],product=product)
            item=int(request.POST['sort'])
        else:
            products=product
            item = 0;
            
        brandsFilter=[b for b in brands if b.name in request.POST]        

        maxPrice=maxNum
        minPrice=0.0
        sp=0
        if 'Max' in request.POST:
            maxPrice=request.POST['Max']
        if 'Min' in request.POST:
            minPrice=request.POST['Min']
        if brandsFilter:   
            products=products.filter(brand_id__in=brandsFilter)
        if 'rating' in request.POST:   
            products=products.filter(rating=request.POST['rating'])
        if 'SpecialOffer' in request.POST:
            products=products.filter(specialOffer=True)
            sp=1;
            
        if products:
            products=products.filter(price__gte=minPrice , price__lte=maxPrice)
        return render(request,"store/ProductList.html",{"products":products,"ProductName":productName[0].name,"brands":brands,"selectItem":item,"maxPrice":maxNum,
                                                        "brandsFiter":brandsFilter,"selectedRate":request.POST['rating'],"specOffer":sp})
