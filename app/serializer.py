from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_id = serializers.IntegerField(source='product.id')
    product_slug = serializers.CharField(source='product.slug')
    product_image = serializers.ImageField(source='product.image')
    product_image2 = serializers.ImageField(source='product.image2')
    product_description = serializers.CharField(source='product.description')
    product_new_price = serializers.CharField(source='product.new_price')
    product_old_price = serializers.CharField(source='product.old_price')
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug','product_name','product_id','product_slug','product_image','product_image2','product_description','product_new_price','product_old_price']

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','new_price', 'old_price', 'is_available','category_name','category_slug','category_id']

    