from django.urls import path
from . import views

urlpatterns = [
    path('addusers', views.addUsers),
    path('getusers', views.getUsers),
]
