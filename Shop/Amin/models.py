from django.db import models


# Create your models here.
class UsersAmin(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
