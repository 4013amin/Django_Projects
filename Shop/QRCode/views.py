import base64
from django.shortcuts import render, get_object_or_404
from .models import Menu
import qrcode
from io import BytesIO
from django.http import HttpResponse


# Create your views here.

def menu_detail(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    return render(request, 'QRCode/menu_detail.html', {'menu': menu})


def generate_qr_code(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    menu_url = request.build_absolute_uri(menu.get_absolute_url())

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(menu_url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    image_bytes = buffer.getvalue()

    response = HttpResponse(image_bytes, content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="menu_qr_{menu_id}.png"'
    return response


def qr_code_page(request):
    # ایجاد یک منوی فیک (اگر وجود نداشته باشد)
    menu, created = Menu.objects.get_or_create(
        id=1,
        defaults={
            'name': 'منوی رستوران تست',
            'description': 'این یک منوی تست است.'
        }
    )

    # ایجاد لینک به صفحه منو
    menu_url = request.build_absolute_uri(f'/menu/{menu.id}/')

    # تولید QR کد
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(menu_url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    image_bytes = buffer.getvalue()

    qr_code_base64 = base64.b64encode(image_bytes).decode('utf-8')

    return render(request, 'QRCode/qr_code_page.html', {
        'menu': menu,
        'qr_code_base64': qr_code_base64,
    })
