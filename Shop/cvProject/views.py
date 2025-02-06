from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.contrib.auth.models import User
from .forms import loginForm


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

            if user is not None:
                login(request, user)
                if request.POST.get('next'):
                    return redirect(request.POST.get('next'))
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                if User.objects.filter(username=username).exists():
                    context = {
                        'username': username,
                        'error': "نام کاربری یا رمز عبور اشتباه است!"
                    }
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.is_superuser = False
                    user.is_staff = False
                    user.save()

                    login(request, user)
                    return render(request, 'index.html')

                return render(request, 'login.html', context)

        return render(request, 'login.html')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'index.html')


def dashboard(request):
    pass
    return render(request, 'dashboard.html')


def contact(request):
    return render(request, 'contact.html')


@login_required
def venue_view(request):
    venues = models.Concert.objects.all()
    return render(request, 'venues.html', {'venues': venues})


@login_required
def venue_detail(request, id):
    venue = get_object_or_404(models.Concert, id=id)
    return render(request, 'venue_detail.html', {'venue': venue})
