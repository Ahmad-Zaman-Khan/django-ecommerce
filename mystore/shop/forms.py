# from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Order


class CustomUserCreationForm(UserCreationForm):

    last_name = forms.CharField(max_length=30, required=True,
                           widget=forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Enter your name'}))
    first_name = forms.CharField(max_length=30, required=True,
                           widget=forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Enter your name'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Enter your email'}))

    password1 = forms.CharField(label="Password", max_length=30, required=True, widget=forms.PasswordInput(
        attrs={'class': 'custom-input', 'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label="Password Confirmation", max_length=30, required=True, widget=forms.PasswordInput(
        attrs={'class': 'custom-input', 'placeholder': 'Confirm your password'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name','last_name', 'password1', 'password2')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['shipping_address', 'payment_method']
