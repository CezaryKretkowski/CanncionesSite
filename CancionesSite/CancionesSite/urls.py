import debug_toolbar
from app.Views.Admin.Admin import AdminView
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', AdminView.as_view(),name="admin"),
    path('', include('app.urls', namespace='app')),
    path('__debug__/', include(debug_toolbar.urls)),

]

