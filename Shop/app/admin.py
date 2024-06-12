from django.contrib import admin
from .models import Users, data

# Register your models here.
admin.site.register(Users)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_name', 'price')
    search_fields = ('name', 'product_name')


@admin.register(data)
class dataAdmin(admin.ModelAdmin):
    list_display = ('name', 'des')
