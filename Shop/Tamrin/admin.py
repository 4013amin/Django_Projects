from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
