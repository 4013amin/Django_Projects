from django.shortcuts import render

from . import models


# Create your views here.

def index(request):
    questions = models.Question.objects.all()
    context = {'questions': questions}
    return render(request, 'index.html', context)
