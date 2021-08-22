from django.db import models
from django.db.models.fields import CharField, DecimalField
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('stale', 'Stale'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)


class Category(models.Model):
    name = CharField(max_length=50, null=False)
    description = models.CharField(max_length=2000)
    slug = models.SlugField(null=False)

    def get_absolute_url(self):
        return reverse('category_details', kwargs={'slug': self.slug})  

    def __str__(self):
        return self.name


class Product(models.Model): 
    product_name = CharField(max_length=50, null=False, default=None)
    description = models.CharField(max_length=2000, default=None)
    picture = models.ImageField(null=False) 
    price = DecimalField(decimal_places=2, max_digits=5, default=0)
    category = models.ForeignKey(Category, on_delete=CASCADE, default=1)
    inventory = models.IntegerField(default=0)

    def has_inventory(self):
        return False
        #return self.inventory > 0  # True or False

    def __str__(self):
        return self.product_name


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices= ORDER_STATUS_CHOICES, default='created')
    sub_total = DecimalField(decimal_places=2, max_digits=5, default=0)
    tax = DecimalField(decimal_places=2, max_digits=5, default=0)
    total = DecimalField(decimal_places=2, max_digits=5, default=0)
    paid = DecimalField(decimal_places=2, max_digits=5, default=0)
    shipping_address = models.TextField(blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)


