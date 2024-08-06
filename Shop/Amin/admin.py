from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.UsersAmin)
class UsersAminAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone']
