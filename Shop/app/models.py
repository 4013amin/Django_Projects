from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="Profile_client")
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class OTP(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="otp")
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.code}"

class Product(models.Model):
    image = models.ImageField(upload_to='product/image')
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
