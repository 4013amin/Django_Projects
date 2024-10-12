from django.urls import path

from .views import sendData, getData
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('sendData/', sendData, name='index'),
                  path('getData', getData)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
