"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_views, name='index'),
    path('accounts/', accounts_views, name='accounts'),
    path('login/', login_views, name='login'),
    path('signup/', signup_views, name='signup'),
    path('products/', product_views, name='products'),
    path('add_index/', add_index_views, name='add_index'),
    path('delete_index/<int:pk>/', delete_index_views, name='delete_index'),
    path('edit_index/<int:pk>/', edit_index_views, name='edit_index'),
    path('add_product/', add_product_views,name='add_product'),
    path('delete_product/<int:pk>/', delete_product_views,name='delete_product'),
    path('cat/', cat_views,name='cat'),
    path('delete_cat/<int:pk>/', delete_cat_views,name='delete_cat'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
