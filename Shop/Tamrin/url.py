from django.urls import path
from . import views
from .Api_View import TastkViewSet

urlpatterns = [
    path('', views.index, name='home'),
    path('list_task', views.list_tasks, name='list_task'),

    path('Api/tasks', TastkViewSet.as_view(), name='tasks'),

]
