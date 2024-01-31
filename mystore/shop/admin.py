from django.contrib import admin


from .models import Product, CartItem, CustomUser, Order, Category, SubCategory

# Now register the new UserAdmin...
# Register the CustomUser model with the default UserAdmin
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(SubCategory)

admin.site.register(Product)

# Register the CartItem model with the admin site
admin.site.register(CartItem)
admin.site.register(Order)
