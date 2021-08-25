from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from store.models import Category, Product
import json



class TestView(TestCase):

    def test_cart_summary_GET(self):
        client =  Client()
        response = client.get(reverse('store:cart'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/cart/summary.html')