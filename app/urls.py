from django.urls import path
from app import views

urlpatterns = [
    path('', views.productsPage, name='productsPage'),
    path('product_detail/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('products/search/', views.search, name='search'),
    path('api_product_detail_view/', views.api_product_detail_view, name='productDetails')
]