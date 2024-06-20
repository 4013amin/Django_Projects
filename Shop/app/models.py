from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    product_name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    date = models.CharField(max_length=20)
    description = models.CharField(max_length=1500)

    def __str__(self):
        return self.name


class user_test(models.Model):
    name = models.CharField(max_length=30)
    number1 = models.CharField(max_length=30)
    number2 = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Login_users(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class data(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    des = models.CharField(max_length=30)

    def __str__(self):
        return self.name
