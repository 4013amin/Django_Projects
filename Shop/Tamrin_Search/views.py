from django.shortcuts import render

from . import models


# Create your views here.
def Home_Data(request):
    data = models.Data.objects.all()
    context = {'data': data}
    return render(request, 'index_data.html', context)
