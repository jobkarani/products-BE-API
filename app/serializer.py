from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    class Meta:
        model = Product
        fields = ['name', 'slug', 'image', 'image2', 'image3', 'description','new_price', 'old_price', 'is_available','category_name']

    