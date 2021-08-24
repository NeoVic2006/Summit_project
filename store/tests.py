from django.test import TestCase

# Create your tests here.

from store.models import Product, Category, Order
from mixer.backend.django import mixer
import pytest


class TestModelCategory(TestCase):
    # def setUp(self): 
    #     self.category = Category.objects.create(
    #         name = "Airplanes",
    #         description = "This is description for airplanes",
    #         )
    
    def test_Category_can_be_created(self):
        category = mixer.blend(Category, name = "Airplanes")
        category_result = Category.objects.last()  
        assert category_result.name ==  "Airplanes"

    def test_Category_str(self):
        category = mixer.blend(Category, name = "Cars")
        category_result = Category.objects.last() 
        assert str(category_result) ==  "Cars"

