from django.contrib import messages

from django.db.models import Q
from django.http import  Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from django.views import View
from django.views.generic import DetailView

from .forms import CustomUserCreationForm
from .models import Product, CartItem, Order, Category, SubCategory


def index(request):

    subcategories = SubCategory.objects.all()[:3]

    allProds = []
    for subcategory in subcategories:
        products = Product.objects.filter(subcategory=subcategory)
        if products:
            allProds.append((subcategory, products))

    context = {'allProds': allProds,}

    return render(request, 'shop/shop_home.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['related_products'] = Product.objects.filter(subcategory=product.subcategory).exclude(pk=product.pk)
        return context


def category_products(request, category_name):
    # Filter products based on the selected category
    category = get_object_or_404(Category, name=category_name)

    # Get products belonging to the selected category
    products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'shop/category_products.html', context)


def subcategory_products(request, subcategory_name):
    subcategory = SubCategory.objects.get(name=subcategory_name)
    products = Product.objects.filter(subcategory=subcategory)
    context = {
        'subcategory': subcategory,
        'products': products
    }
    return render(request, 'shop/category_products.html', context)


class AddToCartView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return HttpResponseRedirect(reverse('cart_view'))


class CartView(View):

    def get(self, request):
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user)
        else:
            return redirect('login')

        return render(request, 'shop/cart.html', {'cart_items': cart_items})


def delete_from_cart(request, item_id):
    CartItem.objects.filter(id=item_id).delete()
    return redirect('cart_view')


def custom_search(request):
    query = request.GET.get('form', '')  # Get the search query from the "formm" input field
    results = []

    if query:
        results = Product.objects.filter(Q(name__icontains=query) | Q(category__name__icontains=query))

    return render(request, 'shop/search_results.html', {'query': query, 'results': results})


def user_logout(request):
    logout(request)
    return redirect('index')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the dashboard or any other page after login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'shop/login.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # Specify the authentication backend
            login(request, user)
            return redirect('index')  # Replace 'home' with  redirect URL
    else:
        form = CustomUserCreationForm()

    return render(request, 'shop/register.html', {'form': form})


class OrderConfirmationView(View):
    template_name = 'shop/order_confirmation.html'

    def post(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)

            # Check if there's an existing order for the user and product
            user = request.user
            existing_order = Order.objects.filter(user=user).first()

            # If an existing order is found, retrieve the shipping address
            if existing_order:
                user_address = existing_order.shipping_address
            else:
                user_address = None

            # Retrieve the quantity from query parameters
            quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not specified

            # Calculate the total price
            total_price = product.price * quantity

            context = {
                'product': product,
                'quantity': quantity,
                'total_price': total_price,
                'user': user,
                'user_address': user_address,

            }

            return render(request, self.template_name, context)
        except Product.DoesNotExist:
            raise Http404("Product does not exist")


# views.py


class PlaceOrderView(View):
    template_name = 'shop/order_history.html'

    def post(self, request):
        # Retrieve user, product, quantity, and other order details
        user = request.user
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not specified

        # Get the user's current shipping address from the form or elsewhere
        current_shipping_address = request.POST.get('shipping_address', '')  # Adjust as needed
        print(current_shipping_address)
        # Create a new Order object with the provided shipping address

        existing_order = Order.objects.filter(user=user, product_id=product_id).first()
        if existing_order:
            # If an existing order is found, update its quantity
            existing_order.quantity += quantity
            existing_order.save()
        else:
            # If no existing order is found, create a new one
            product = Product.objects.get(id=product_id)
            order = Order(
                user=user,
                product=product,
                quantity=quantity,
                shipping_address=current_shipping_address,
                payment_method="Cash on Delivery",
                order_date=timezone.now(),
            )
            order.save()
        return redirect('orders-history')


class OrderHistoryView(View):
    template_name = 'shop/order_history.html'

    def get(self, request):
        user = request.user if request.user.is_authenticated else None
        if user:
            orders = Order.objects.filter(user=user)
            for order in orders:
                # Calculate the total price for each order
                order.total_price = order.product.price * order.quantity
        else:
            orders = []

        context = {
            'user': user,
            'orders': orders,
        }

        return render(request, self.template_name, context)
