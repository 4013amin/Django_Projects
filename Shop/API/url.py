from django.urls import path
from . import views

urlpatterns = [
    path('addProfile/', views.Profile.as_view()),
]
