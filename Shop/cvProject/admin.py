from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password')
