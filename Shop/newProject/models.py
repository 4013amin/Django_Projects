from django.db import models


# Create your models here.
class newData(models.Model):
    image = models.ImageField(upload_to='images/')
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return self.name
