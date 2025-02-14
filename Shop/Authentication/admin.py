from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.ProfileApi)
class ProfileApiAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user',)
