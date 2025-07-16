from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from . import forms
from django.contrib import messages
from . import models


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = forms.Profile_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('phone')

            with transaction.atomic():
                request.user.username = username.lower()
                request.user.save()

                profile, created = models.Profile.objects.get_or_create(user=request.user)
                profile.phone = phone
                profile.save()

                if created:
                    messages.success(request, 'Profile created successfully')
                else:
                    messages.success(request, 'Profile updated successfully')

            return redirect('home')
        else:
            messages.error(request, 'Form is not valid')
    else:
        form = forms.Profile_form()

    return render(request, 'index.html', {'form': form})




def index(request):
    if request.method == "POST":
        form = forms.Tasks_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added")
            return redirect("list_task")
    else:
        form = forms.Tasks_form()

    return render(request, 'index.html', context={'form': form})


def list_tasks(request):
    task = models.Tasks.objects.all()
    return render(request, 'list.html', {'tasks': task})
