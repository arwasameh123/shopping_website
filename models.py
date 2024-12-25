from django.db import models

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, default='product_images/placeholder.png')

    def __str__(self):
        return self.name



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product = models.CharField(max_length=200)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Shipped', 'Shipped'),
            ('Delivered', 'Delivered'),
        ],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Tracks when the order is created

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"
