from django.shortcuts import render

from . import models
from .forms import Search_form


# Create your views here.
def Home_Data(request):
    search = Search_form(request.GET)
    if search.is_valid():
        search_results = search.cleaned_data["text_filed"]
        data_search = models.Data.objects.filter(username__icontains=search_results)

    else:
        data_search = models.Data.objects.all()

    context = {'data': data_search, 'search': search}
    return render(request, 'index_data.html', context)
