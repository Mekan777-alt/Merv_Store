from django.urls import path
from .views import products, categories

app_name = 'products'

urlpatterns = [
    path('products/', products, name='products'),
    path('categories/', categories, name='categories')
]