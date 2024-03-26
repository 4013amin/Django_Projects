from django.urls import path
from .views import create_user, get_all_users
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('create_user', create_user),
    path('get_all_users', get_all_users)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
