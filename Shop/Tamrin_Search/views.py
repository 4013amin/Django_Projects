from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import reverse

from . import models
from .forms import Search_form


def Home_Data(request):
    search = Search_form(request.GET)
    if search.is_valid():
        search_results = search.cleaned_data["text_filed"]
        data_search = models.Data.objects.filter(username__icontains=search_results)

        if not data_search.exists():
            message = "دیتا ها پیدا نشد!"
        else:
            message = ""
    else:
        data_search = models.Data.objects.all()
        message = ""

    context = {'data': data_search, 'search': search, 'message': message}
    return render(request, 'index_data.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "Login_form.html")
        else:
            context = {
                "username": username,
                "message": "نام کاربری یا رمز عبور اشتباه است."
            }
            return render(request, "Login_form.html", context)
    else:
        return render(request, "Login_form.html")


def getData(request):
    search = Search_form(request.GET)
    if search.is_valid():
        search_results = search.cleaned_data["text_filed"]
        data = models.Data.objects.filter(name__icontains=search_results)
    else:
        data = models.Data.objects.all()

    context = {'users': data}
    return render(request, "Data_form.html", context)
