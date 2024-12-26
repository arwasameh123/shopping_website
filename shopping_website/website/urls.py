from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from website.views import sign_up, SignInView

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-in/', views.SignInView.as_view(), name='sign_in'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),

]
