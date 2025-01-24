from django.urls import path
from .views import generate_qr_code, menu_detail, qr_code_page

urlpatterns = [
    path('', qr_code_page, name='qr_code_page'),
    path('menu/<int:menu_id>/', menu_detail, name='menu_detail'),
    path('menu/<int:menu_id>/qr/', generate_qr_code, name='generate_qr_code'),
]