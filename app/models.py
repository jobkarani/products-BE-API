from django.db import models
from django.urls import reverse
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = ImageField(manual_crop="800x800")
    image2 = ImageField(blank=True, manual_crop="800x800")
    image3 = ImageField(blank=True, manual_crop="800x800")
    description = models.TextField(max_length=4000)
    new_price = models.FloatField()
    old_price = models.FloatField()
    is_available = models.BooleanField(default = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name

class BuyMpesa(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.product