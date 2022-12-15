from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','new_price', 'old_price', 'is_available','category_name','category_slug','category_id']

    