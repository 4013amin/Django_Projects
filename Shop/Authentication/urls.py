from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('register/', views.register),
                  path('users/', views.Profile.as_view(), name='profile-list'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
