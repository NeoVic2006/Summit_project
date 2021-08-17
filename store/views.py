from django.shortcuts import render
from django.views import generic
from store.models import Categories, Products
from store.forms import CategoryForm
from django.urls.base import reverse_lazy
# Create your views here.



class Category(generic.ListView):
    model = Categories
    template_name = 'store/main.html'
    context_object_name = 'category_key'


class CategoryUpdate(generic.UpdateView):
    model = Categories
    template_name = 'store/category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('store:list_category')
    

class CategoryDetail(generic.DetailView):
    model = Categories
    template_name = 'store/category_detail.html'


class CategoryCreate(generic.CreateView):
    model = Categories
    template_name = 'store/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('store:list_category')




class Product(generic.ListView):
    model = Products
    template_name = 'store/all_products.html'
    # Here we are sending only products_key context to template. There is no 'category_key' data sent to be used by main.html
    # so Either a) send  extra_context  'category_key' to this template
    # or b) use the FK relationship between the category and products and get the related products in the template 
    context_object_name = 'products_key'
    extra_context = {'category_key':Categories.objects.all}
