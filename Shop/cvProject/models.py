from django.db import models


# Create your models here.
class concert(models.Model):
    image = models.ImageField(upload_to='cvProject/images/', null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    time = models.TimeField()

    def __str__(self):
        return self.title


class users(models.Model):
    username = models.CharField(max_length=100)
    password = models.IntegerField()

    def __str__(self):
        return self.username
