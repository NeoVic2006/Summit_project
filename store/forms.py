from django import forms
from django.forms import fields
from store.models import Category, Order
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

