from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','new_price', 'old_price', 'is_available','category_name','category_slug']

    