from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from app.models import *
from .serializer import *
from .pagination import *
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.

def productsPage(request, category_slug=None):
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
        'categories':categories,
        'products':products,
        'product_count':product_count,
    }
    return render(request, 'products.html', context)

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

    return render(request, 'productDetails.html', context)

def search(request):
    products = 0
    product_count = 0
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            products= Product.objects.order_by('-name').filter(Q(description__icontains=keyword) | Q(name__icontains=keyword))
            product_count = products.count()
        elif keyword != keyword :

            return HttpResponse('Ooops no products found with that keyword :(  Try another Keyword :)')

    ctx={
        'products':products,
        'product_count':product_count,
    }
    return render(request,'products.html', ctx)

@api_view(['GET',])
def api_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def api_categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getProductDetails(request, product_id):
    if request.method == "GET":
        product= Product.objects.filter(id = product_id)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getProductsByCategory(request, category_id):
    if request.method == "GET":
        catproducts= Product.objects.filter( id= category_id )
        serializer = ProductSerializer(catproducts, many=True)
        return Response(serializer.data)