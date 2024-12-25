from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('products/', views.manage_products, name='manage_products'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('users/', views.manage_users, name='manage_users'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('orders/', views.view_orders, name='view_orders'),
    path('orders/update/<int:order_id>/', views.update_order_status, name='update_order_status'),
]
