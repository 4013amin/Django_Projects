from django.contrib import admin
from .models import Users

# Register your models here.
admin.site.register(Users)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_name', 'price')
    search_fields = ('name', 'product_name')
