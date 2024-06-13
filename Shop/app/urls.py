from django.urls import path
from .views import Search , get_data_by_id
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Search, name='index'),
    path('data_id/<int:pk>', get_data_by_id, name='data_id'),
    # path('create_user', views.create_user),
    # path('get_all_users', views.get_all_users),
    # path('update_user/<pk>', views.update_user),
    # path('delete_all_user', views.delete_all_user),
    # path('delete_user/<pk>', views.delete_user_id),
    # path('get_user_by_id/<pk>', views.get_user_by_id),
    # path('send_request', views.send_request),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
