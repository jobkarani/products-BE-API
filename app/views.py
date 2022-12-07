from django.shortcuts import get_object_or_404, render

from app.models import *

# Create your views here.

def productsPage(request, category_slug=None,product_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'product_count':product_count,
    }
    return products

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