from django.urls import path
from .views import sendRequest
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('sendRequest/', views.sendRequest, name='send_request'),
                  path('RegisterUser/', views.RegisterUser, name='send_request'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
