from django.db import models


# Create your models here.
class ProfileUser(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.username
