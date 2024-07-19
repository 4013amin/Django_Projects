from django.urls import path
from .views import sendRequest
from . import views
urlpatterns = [
    path('sendRequest/', views.sendRequest, name='send_request'),
]
