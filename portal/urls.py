from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'my_products', views.my_products, name='my_products'),
    path(r'products/new', views.products_new, name='products_new'),
]
