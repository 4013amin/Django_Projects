from django.contrib import admin
from .models import newData, BannerData


# Register your models here.
@admin.register(newData)
class NewDataAdmin(admin.ModelAdmin):
    list_display = ['title', 'name']


@admin.register(BannerData)
class BannerDataAdmin(admin.ModelAdmin):
    list_display = ['title']
