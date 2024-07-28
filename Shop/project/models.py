from django.db import models


# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
