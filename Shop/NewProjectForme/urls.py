from django.urls import path
from .views import AddUsersView, GetUsersView, LoginView

urlpatterns = [
    path('addusers', AddUsersView.as_view(), name='add_users'),
    path('getusers', GetUsersView.as_view(), name='get_users'),
    path('login', LoginView.as_view(), name='login'),
]
