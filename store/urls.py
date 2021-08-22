from django.contrib import admin
from django.urls import path, re_path
from store.views import Categories, CategoryUpdate, CategoryDetail, CategoryCreate, Products, cart_summary, cart_add


app_name ='store'
urlpatterns = [
    
    path('', Categories.as_view(), name='list_category'),  
    path('cart/', cart_summary, name='cart'),  
    path('cart_add/', cart_add, name='cart_add'),
    #path('checkout/', order_checkout_view),

    path('product/<int:pk>/', Products.as_view(), name='product'), 

    path('create/', CategoryCreate.as_view(), name='category_create'),     

    path('<slug:slug>/update/', CategoryUpdate.as_view(), name='category_update'),

    path('<slug:slug>/', CategoryDetail.as_view(), name='category_details'),  
    
]
