from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Product  # Import the Product model from dashboard
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .models import Cart
from django.contrib.auth.decorators import login_required
from dashboard.models import Order
from django.contrib.auth import logout
from django.shortcuts import redirect
# Home Page
def home(request):
    products = Product.objects.all()[:6]
    return render(request, 'website/home.html', {'products': products})

# Products Page
def products(request):
    products = Product.objects.all()
    return render(request, 'website/products.html', {'products': products})

# Product Detail Page
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'website/product_detail.html', {'product': product})

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'website/sign_up.html', {'form': form})

class SignInView(LoginView):
    template_name = 'website/sign_in.html'

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    cart_details = []

    # Calculate total price for each item
    for item in cart_items:
        cart_details.append({
            'product': item.product,
            'quantity': item.quantity,
            'total_price': item.product.price * item.quantity
        })

    # Calculate total cart price
    total_price = sum(item['total_price'] for item in cart_details)

    return render(request, 'website/cart.html', {
        'cart_details': cart_details,
        'total_price': total_price,
    })
@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('cart')

from dashboard.models import Order

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    if request.method == 'POST':
        for item in cart_items:
            Order.objects.create(
                customer_name=request.user.username,
                product=item.product.name,
                quantity=item.quantity,
                total_price=item.product.price * item.quantity,
                status='Pending'
            )
        cart_items.delete()  # Clear cart after checkout
        return redirect('order_confirmation')
    return render(request, 'website/checkout.html', {'cart_items': cart_items})

@login_required
def order_confirmation(request):
    return render(request, 'website/order_confirmation.html')


def custom_logout(request):
    logout(request)
    return redirect('home')