from django.urls import path
from .views import sendRequest

urlpatterns = [
    path('sendRequest', sendRequest),
]
