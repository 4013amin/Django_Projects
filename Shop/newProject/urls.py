from django.urls import path

from . import views

urlpatterns = [
    path('sendNewData/', views.sendNewData),
    path('getNewData/', views.getAllNewData),
    path('deleteNewData/<int:pk>/', views.deleteNewData),
]
