from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from .Views.Home import Home
from .Views.Login.Login import Login
from .Views.Login.LogOut import LogOut
from .Views.User.UserView import UserView
from .Views.Products.SubCategoryView import SubCategoryView
from .Views.Registration.Registration import RegistrationView
from .Views.Products.ProductList import ProductList
from .Views.Products.ProductDetails import ProductDetails
from .Views.Products.CartView import CartView
from .Views.Products.Customization import CustomizationView


app_name = 'app'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register', RegistrationView.as_view(), name='registry'),
    path('login', Login.as_view(), name='login'),
    path('logout', LogOut.as_view(), name='logout'),
    path('userview',UserView.as_view()),
    path('category/<int:pk>/',SubCategoryView.as_view(),name='SubCategoryView'),
    path('subCategory/<int:pk>/',ProductList.as_view(),name='ProductList'),
    path('Product/<int:pk>/',ProductDetails.as_view(),name='ProductDetails'),
    path('Customozation/<int:pk>/',CustomizationView.as_view(),name='Customization'),
    path('Cart/add/<int:pk>/',CartView.add_To_Card,name='Cart/add'),
    path('Cart/',CartView.as_view(),name='Cart'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
