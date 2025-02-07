from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('venues/', views.venue_view, name='venues'),
    path('venues/<int:id>/', views.venue_detail, name='venue_detail'),
    path('venuesEdit/<int:id>/', views.venuesEdit_View, name='venuesEdit'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('contact', views.contact, name='contact'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
