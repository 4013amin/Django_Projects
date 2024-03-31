from django.urls import path
from .views import create_user, get_all_users, update_user, delete_user_id, delete_all_user, get_user_by_id
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('create_user', create_user),
    path('get_all_users', get_all_users),
    path('update_user/<pk>', update_user),
    path('delete_all_user', delete_all_user),
    path('delete_user/<pk>', delete_user_id),
    path('get_user_by_id/<pk>', get_user_by_id)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
