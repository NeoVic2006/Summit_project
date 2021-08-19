from django.db import models
from django.db.models.fields import CharField, DecimalField
from django.db.models.deletion import CASCADE
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = CharField(max_length=50, null=False)
    description = models.CharField(max_length=2000)
    slug = models.SlugField(null=False)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_details', kwargs={'slug': self.slug})



class Product(models.Model): 
    product_name = CharField(max_length=50, null=False, default=None)
    description = models.CharField(max_length=2000, default=None)
    picture = CharField(max_length=2000, default=None) # try to make a imagefield 
    price = DecimalField(decimal_places=2, max_digits=5, default=0)
    category = models.ForeignKey(Category, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.product_name



