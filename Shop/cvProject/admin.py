from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Profile)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'credit')


@admin.register(models.Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')


@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message')


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'concert')
