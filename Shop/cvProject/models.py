from django.db import models


class Concert(models.Model):
    image = models.ImageField(upload_to='cvProject/images/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    time = models.TimeField()
    capacity = models.PositiveIntegerField(null=True, blank=True)  # اضافه کردن ظرفیت

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('venue_detail', args=[str(self.id)])


class users(models.Model):
    username = models.CharField(max_length=100)
    password = models.IntegerField()

    def __str__(self):
        return self.username
