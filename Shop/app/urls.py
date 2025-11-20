from django.urls import path
from . import views

urlpatterns = [
    path('' , views.login_view , name='login_view'),
    path('home/' , views.home_view , name='home'),
]
