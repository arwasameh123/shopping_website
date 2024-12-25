from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, User, Order
from django.http import HttpResponse
from datetime import date
from django.db.models import Sum

# Admin Dashboard View
def admin_dashboard(request):
    # Total counts
    total_products = Product.objects.count()
    total_users = User.objects.count()

    # Calculate total revenue for today
    today = date.today()
    today_revenue = Order.objects.filter(created_at__date=today).aggregate(Sum('total_price'))['total_price__sum'] or 0

    context = {
        'total_products': total_products,
        'total_users': total_users,
        'today_revenue': today_revenue,  # Pass total revenue to the template
    }
    return render(request, 'dashboard/admin_dashboard.html', context)

# Manage Products
def manage_products(request):
    products = Product.objects.all()
    return render(request, 'dashboard/manage_products.html', {'products': products})

# Add Product
def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        stock = request.POST['stock']
        Product.objects.create(name=name, description=description, price=price, stock=stock)
        return redirect('manage_products')
    return render(request, 'dashboard/add_product.html')

# Delete Product
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('manage_products')

# Manage Users
def manage_users(request):
    users = User.objects.all()
    return render(request, 'dashboard/manage_users.html', {'users': users})

# Add User
def add_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        User.objects.create(name=name, email=email)
        return redirect('manage_users')
    return render(request, 'dashboard/add_user.html')

# Delete User
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('manage_users')

def view_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'dashboard/view_orders.html', {'orders': orders})

# Update Order Status
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.status = request.POST.get('status')
        order.save()
        return redirect('view_orders')
    return render(request, 'dashboard/update_order_status.html', {'order': order})