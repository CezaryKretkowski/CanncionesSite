from django.views.generic import TemplateView
from ..Entities.Dictionary.SubCategory import SubCategory
from ..Entities.Dictionary.Category import Category
from ..Utilities.Utilities import Utilities

class Home(TemplateView):
    template_name = "store/Home.html"
        
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        try:
            data=Category.objects.all()
            subCat=SubCategory.objects.all()
        except Category.DoesNotExist:
            data=[]
            subCat=[]
        categories=Utilities().chanks(data,3)
        context['Categories']=categories        
        context['SubCategory']=subCat
        return context


    