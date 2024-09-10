from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import reverse

from . import models
from .forms import Search_form, FormEdit


# def Home_Data(request):
#     search = Search_form(request.GET)
#     if search.is_valid():
#         search_results = search.cleaned_data["text_filed"]
#         data_search = models.Data.objects.filter(username__icontains=search_results)
#
#         if not data_search.exists():
#             message = "دیتا ها پیدا نشد!"
#         else:
#             message = ""
#     else:
#         data_search = models.Data.objects.all()
#         message = ""
#
#     context = {'data': data_search, 'search': search, 'message': message}
#     return render(request, 'index_data.html', context)


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


def EditFormView(request):
    data = models.Data.objects.all()
    if request.method == "POST":
        data_edit = FormEdit(request.POST, request.files, instance=data)
        if data_edit.is_valid():
            data_edit.save()
            return render(request, "Edit_form.html")
        else:
            data_edit = FormEdit(instance=data)

        context = {
            "data": data_edit,
            "Image_Editor": models.Data.image
        }

        return render(request, "Edit_form.html", context)
