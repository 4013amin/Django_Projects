from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from . import models


# Create your views here.

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
