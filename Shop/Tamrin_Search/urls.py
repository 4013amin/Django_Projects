from django.urls import path

from . import views
from . import models

urlpatterns = [
    path('', views.Home_Data, name='index'),
    path('login/', views.login_view, name='login'),
]
