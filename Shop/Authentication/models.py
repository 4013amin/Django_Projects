from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ProfileApi(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.FloatField(default=0)

    image = models.ImageField(upload_to='images/')
    MAN = 1
    WOMAN = 2

    STATUS_CHOICES = (
        (MAN, "مرد"),
        (WOMAN, "خانم"),
    )
    gender = models.IntegerField(choices=STATUS_CHOICES, default=MAN)

    def __str__(self):
        return self.user.username
