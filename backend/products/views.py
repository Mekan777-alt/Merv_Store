from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    context = {
        'title': 'MerwStore | Начало',
    }
    return render(request, 'products/index.html', context)


def products(request):
    return render(request, 'products/product.html')


def categories(request):
    return render(request, 'products/categories.html')
