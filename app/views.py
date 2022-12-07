from django.shortcuts import render

from app.models import *

# Create your views here.

def product_detail(request, category_slug, product_slug):

    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        products = Product.objects.all().filter(is_available=True)

    except Exception as e:
        raise e

    context = {
    'single_product': single_product,
    'products':products,
    }

    return single_product