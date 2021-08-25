from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import Categories, CategoryUpdate, CategoryDetail, CategoryCreate, Products, cart_summary, cart_add



class TestUrls(SimpleTestCase):

    # path('', Categories.as_view(), name='list_category'),  
    def test_list_category_url_is_resolves(self):
        url = reverse('store:list_category')
        self.assertEqual(resolve(url).func.view_class, Categories)  # testing Class View Url

    #  path('cart/', cart_summary, name='cart'), 
    def test_cart_url_is_resolves(self):
        url = reverse('store:cart')
        self.assertEqual(resolve(url).func, cart_summary)  # testing function View Url

    # path('<slug:slug>/', CategoryDetail.as_view(), name='category_details'),  
    def test_category_details_url_is_resolves(self):
        url = reverse('store:category_details', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, CategoryDetail)  # testing Slug parametr
        