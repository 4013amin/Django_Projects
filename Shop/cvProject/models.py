from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Concert(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    time = models.TimeField()
    capacity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('venue_detail', args=[str(self.id)])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.FloatField(default=0)

    image = models.ImageField(upload_to='cvProject/images/', null=True, blank=True)
    MAN = 1
    WOMAN = 2

    STATUS_CHOICES = (
        (MAN, "مرد"),
        (WOMAN, "خانم"),
    )
    gender = models.IntegerField(choices=STATUS_CHOICES, default=MAN)

    def __str__(self):
        return self.user.username


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    file = models.FileField(upload_to='media/files/', null=True, blank=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.concert.title}"
