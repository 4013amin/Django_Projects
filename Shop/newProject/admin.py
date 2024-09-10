from django.contrib import admin
from .models import newData


# Register your models here.
@admin.register(newData)
class NewDataAdmin(admin.ModelAdmin):
    list_display = ['username', 'number']
