from django.urls import path
from app import views

urlpatterns = [
    path('api_product_detail_view/', views.api_product_detail_view, name='productDetails'),
]