from django.contrib import admin
from django import forms
from django.contrib.auth import get_user_model

from .models import Product, CartItem, CustomUser, Order, Category, SubCategory

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin





# Now register the new UserAdmin...
# Register the CustomUser model with the default UserAdmin
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(SubCategory)
# admin.site.register(get_user_model())
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.

# Register the Product model with the admin site
admin.site.register(Product)

# Register the CartItem model with the admin site
admin.site.register(CartItem)
admin.site.register(Order)
