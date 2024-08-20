from django.db import models


# Create your models here.
class newData(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    description = models.TextField()
    title = models.CharField(max_length=100)
    txt = models.TextField()

    def __str__(self):
        return self.name


class BannerData(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
