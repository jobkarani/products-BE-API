from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

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
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name