from django.shortcuts import render
from django.views import generic
from store.models import Category, Product
from store.forms import CategoryForm
from django.urls.base import reverse_lazy
# Create your views here.



class Categories(generic.ListView):
    model = Category
    template_name = 'store/main.html'
    context_object_name = 'category_key'


class CategoryUpdate(generic.UpdateView):
    model = Category
    template_name = 'store/category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('store:list_category')
    
    
class CategoryDetail(generic.DetailView):
    model = Category
    template_name = 'store/category_detail.html'
    extra_context = {'category_key':Category.objects.all, 
                     'product_key':Product.objects.filter(category_id=2)}      # how to add proper filter for choosen category. I need help with this 
    # you receive slug here in the url. So use the category slug value to filter the products like Product.objects.filter(category__slug=slug)


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
