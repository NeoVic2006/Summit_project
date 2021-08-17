from django.db import models
from django.db.models.fields import CharField, DecimalField
from django.db.models.deletion import CASCADE
# Create your models here.


class Categories(models.Model):
    name = CharField(max_length=50, null=False)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.name



class Products(models.Model):
    product_name = CharField(max_length=50, null=False, default=None)
    description = models.CharField(max_length=2000, default=None)
    picture = CharField(max_length=2000, default=None) # try to make a imagefield 
    price = DecimalField(decimal_places=2, max_digits=5, default=0)
    category = models.ForeignKey(Categories, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.product_name
