from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('senRegister', views.sendRegister),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
