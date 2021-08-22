from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views import generic
from store.models import Category, Product
from store.forms import CategoryForm, CreateUserForm
from django.urls.base import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.


def cart_summary(request):
    return render(request, 'store/cart/summary.html')


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
         product_id = int(request.POST.get('productid'))
         product = get_object_or_404(Product, id=product_id)
         cart.add(product=product)
         response = JsonResponse({'test':'data'})
         print(response)
         return response


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product):
        product_id = product.id
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price)}
        self.session.modified = True





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


class Products(generic.DetailView):
    model = Product
    template_name = 'store/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'category_key': Category.objects.all})
        context.update({'product_key': Product.objects.filter(pk=self.kwargs.get('pk'))})
        return context


