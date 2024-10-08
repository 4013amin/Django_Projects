from django.db import models


# Create your models here.
class Data(models.Model):
    image = models.ImageField(upload_to='images/')
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
