from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('list_task', views.list_tasks, name='list_task'),
]
