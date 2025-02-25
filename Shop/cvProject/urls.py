from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('venues/', views.venue_view, name='venues'),
    path('venues/<int:id>/', views.venue_detail, name='venue_detail'),
    path('venuesEdit/<int:id>/', views.venuesEdit_View, name='venuesEdit'),
    path('reserve/<int:id>/', views.reserve_concert, name='reserve_concert'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboardEdit', views.dashboard_Edit, name='dashboardEdit'),
    path('contact', views.contact, name='contact'),
    path('login', views.login_view, name='login'),
    path('addData', views.GetAllData.as_view()),
    path('admin/dashboard/', views.admin_dashboard_View, name='admin_dashboard'),
    path('register/', views.register_view, name='register'),
    path('contact/', views.contact_Us_view, name='contact'),
    path('logout', views.logout_view, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
