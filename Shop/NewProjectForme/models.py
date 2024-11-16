from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    password = models.CharField(max_length=30)
    passW = models.CharField(max_length=30)

    def __str__(self):
        return self.username
    

class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=300)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=30)
    quantity = models.IntegerField()
    rating = models.FloatField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
