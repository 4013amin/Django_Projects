from django.urls import path

from .Api_View import TastkViewSet

urlpatterns = [
    path('Api/tasks', TastkViewSet.as_view(), name='tasks'),
]
