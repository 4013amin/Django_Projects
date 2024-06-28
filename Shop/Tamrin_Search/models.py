from django.db import models


# Create your models here.
class Data(models.Model):
    username = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    Date = models.DateField()
    file = models.FileField(upload_to="data/")

    def __str__(self):
        return self.title
