from django.db.models.fields import SlugField
from django.shortcuts import render
from django.views import generic
from store.models import Category, Product
from store.forms import CategoryForm
from django.urls.base import reverse_lazy
# Create your views here.


class User():
    pass


class Categories(generic.ListView):
    model = Category
    template_name = 'store/main.html'
    context_object_name = 'category_key'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'product_key': Product.objects.all})
        return context


class CategoryUpdate(generic.UpdateView):
    model = Category
    template_name = 'store/category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('store:list_category')
    
    
class CategoryDetail(generic.DetailView):
    model = Category
    template_name = 'store/category_detail.html'
    # extra_context = {'category_key':Category.objects.all, 
    #                  'product_key':Product.objects.filter(category__slug=test)}   # how to add proper filter for choosen category. I need help with this 


    def get_context_data(self, **kwargs):
        for x, y in kwargs.items():
            name = y
        context = super().get_context_data(**kwargs)
        context.update({'category_key': Category.objects.all})
        context.update({'product_key': Product.objects.filter(category__slug=name)})
        return context


class CategoryCreate(generic.CreateView):
    model = Category
    template_name = 'store/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('store:list_category')




class Products(generic.ListView):
    model = Product
    template_name = 'store/all_products.html'
    context_object_name = 'products_key'
    extra_context = {'category_key':Category.objects.all}
