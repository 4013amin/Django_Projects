from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from . import serilizer
from rest_framework.response import Response
from rest_framework import status
from . import models
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import loginForm, Edit_Form_venues, RegisterForm, Form_Contact_Us, Edit_Dashboard, ProfileEditForm


# Create your views here.
def home(request):
    pass
    return render(request, 'index.html')


def login_view(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is None:
                user = User.objects.create_user(username=username, password=password)
                user.is_superuser = False
                user.is_staff = False
                user.save()

            login(request, user)  # لاگین کاربر

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        # خطای ورود
        context = {
            'username': username,
            'error': "نام کاربری یا رمز عبور اشتباه است!"
        }
        return render(request, 'login.html', context)

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'index.html')


@login_required
def dashboard(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        profile = models.Profile.objects.create(user=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def dashboard_Edit(request):
    if request.method == "POST":
        form = Edit_Dashboard(request.POST, request.FILES, instance=request.user.profile)
        formUser = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid() and formUser.is_valid():
            form.save()
            formUser.save()
            return redirect('dashboard')
    else:
        form = Edit_Dashboard(instance=request.user.profile)
        formUser = ProfileEditForm(instance=request.user)

    # Check if the image is present before accessing its URL
    profile_image = None
    if request.user.profile.image:
        profile_image = request.user.profile.image.url

    context = {
        'form': form,
        'profile_image': profile_image,
        'formUser': formUser,
    }
    return render(request, 'profileEdit.html', context)


def contact(request):
    return render(request, 'contact.html')


def venue_view(request):
    venues = models.Concert.objects.all()

    category = request.GET.get('category', '').strip()
    max_Price = request.GET.get('max_price', '').strip()
    search = request.GET.get('search', '')

    if category:
        venues = venues.filter(category=category)

    if max_Price:
        try:
            max_Price = int(max_Price)
            venues = venues.filter(price__lte=max_Price)  # Corrected to filter by max price
        except ValueError:
            return redirect('venues')

    if search:
        venues = venues.filter(title__icontains=search)

    context = {
        'venues': venues,
        'selected_category': category,  # Set to 'category' directly
        'max_price': str(max_Price) if max_Price else '50000',
        'search': search
    }

    return render(request, 'venues.html', context)


@login_required
def venuesEdit_View(request, id):
    venue = get_object_or_404(models.Concert, id=id)

    if request.user.username != "Amin" or not request.user.is_superuser:
        return render(request, '403.html', status=403)

    if request.method == "POST":
        editForm = Edit_Form_venues(request.POST, request.FILES, instance=venue)
        if editForm.is_valid():
            editForm.save()
            return render(request, 'venues.html', {'editForm': editForm})
    else:
        editForm = Edit_Form_venues(instance=venue)

    context = {
        'editForm': editForm,
        'Image': models.Concert.image
    }

    return render(request, 'venuesEdit.html', context)


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            # بررسی تکراری بودن نام کاربری
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'این نام کاربری قبلاً استفاده شده است.')
            else:
                user = models.User.objects.create_user(
                    username=username,
                    password=form.cleaned_data.get('password'),
                    email=form.cleaned_data.get('email'),
                )
                user.save()
                profile = models.Profile.objects.create(user=user,
                                                        credit=form.cleaned_data.get('credit'),
                                                        image=form.cleaned_data.get(
                                                            'image'))  # تصویر و اعتبار ذخیره می‌شود.
                profile.save()
                return redirect('venues')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'register.html', context)


# Form_Contact_Us
def contact_Us_view(request):
    if request.method == "POST":
        form = Form_Contact_Us(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'contact_success.html')
    else:
        form = Form_Contact_Us()
        return render(request, 'contact.html', {'form': form})


def venue_Index_view(request):
    venues = models.Concert.objects.all()[:5]
    context = {
        'venues': venues
    }
    return render(request, 'index.html', context)


@login_required
def venue_detail(request, id):
    venue = get_object_or_404(models.Concert, id=id)
    return render(request, 'venue_detail.html', {'venue': venue})


# reserve
def reserve_concert(request, id):
    concerts = get_object_or_404(models.Concert, id=id)
    profile = models.Profile.objects.get(user=request.user)

    if models.Booking.objects.filter(user=request.user, concert=concerts).exists():
        messages.error(request, "شما قبلاً برای این کنسرت رزرو کرده‌اید.")
        return redirect('venue_detail', id=concerts.id)

    if concerts.capacity is not None and concerts.capacity <= 0:
        messages.error(request, "ظرفیت این کنسرت تکمیل شده است.")
        return redirect('venue_detail', id=concerts.id)

    if profile.credit < concerts.price:
        messages.error(request, "اعتبار شما کافی نیست.")
        return redirect('venue_detail', id=concerts.id)

    profile.credit -= concerts.price
    profile.save()

    models.Booking.objects.create(user=request.user, concert=concerts)

    if concerts.capacity is not None:
        concerts.capacity -= 1
        concerts.save()

    messages.success(request, "رزرو با موفقیت انجام شد.")
    return redirect('venue_detail', id=concerts.id)


# for admin
def loginAdmin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin/login.html', {'error': 'نام کاربری یا رمز عبور اشتباه است!'})
    return render(request, 'admin/login.html')


@login_required
def admin_dashboard_View(request):
    if not request.user.is_superuser:
        return render(request, '403.html', status=403)

    concerts = models.Concert.objects.all()
    concert_data = []
    for concert in concerts:
        concert_data.append({
            'title': concert.title,
            'reserved_tickets': concert.reserved_tickets,
            'remaining_capacity': concert.remaining_capacity,
            'price': concert.price,
            'category': concert.category
        })

    context = {
        'concert_data': concert_data
    }

    return render(request, 'dashboardAdmin.html', context)
