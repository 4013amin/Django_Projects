from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('venues', views.home, name='venues'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('contact', views.contact, name='contact'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
