from django.contrib import admin
from django.urls import path, re_path
from store.views import Categories, CategoryUpdate, CategoryDetail, CategoryCreate, Products


app_name ='store'
urlpatterns = [
    path('', Categories.as_view(), name='list_category'),  
    path('create/', CategoryCreate.as_view(), name='category_create'),           
    re_path(r'^(?P<pk>\d+)/update/$', CategoryUpdate.as_view(), name='category_update'),
    path('products/', Products.as_view(), name='list_products'), 
    path('<slug:slug>/', CategoryDetail.as_view(), name='category_details'),   # here you are passing around the slug value of category. So you can filter() the products based on this field. 
    #re_path('<str:category_name>/',)
    
]
