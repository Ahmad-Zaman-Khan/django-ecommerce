from django.urls import path, include

from . import views
from .views import ProductDetailView, AddToCartView, CartView, OrderConfirmationView, PlaceOrderView, OrderHistoryView, \
    subcategory_products

urlpatterns = [
    path("", views.index, name="index"),

    path("t/", views.index3, name="index3"),
    path('subcategory/<str:subcategory_name>/', views.subcategory_products, name='subcategory_products'),
    path('category/<str:category_name>/', views.category_products, name='category_products'),
    path('custom_search/', views.custom_search, name='custom_search'),


    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('order-confirmation/<int:product_id>/', OrderConfirmationView.as_view(), name='order_confirmation'),
    path('place-order/', PlaceOrderView.as_view(), name='place-order'),
    path('orders-history/', OrderHistoryView.as_view(), name='orders-history'),
    path('accounts/', include('django.contrib.auth.urls')),


    path('cart/', CartView.as_view(), name='cart_view'),
    path('add-to-cart/<int:product_id>/', AddToCartView.as_view(), name='add-to-cart'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('cart/delete/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('logout/', views.user_logout, name='logout'),
]
