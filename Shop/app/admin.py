from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Profile)
class Profile_Admin(admin.ModelAdmin):
    list_display = ['user', 'name', 'phone']
    
    
@admin.register(models.Product)
class Product_Admin(admin.ModelAdmin):
    list_display = ['name' , 'price' ,'description']