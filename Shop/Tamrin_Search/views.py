from django.shortcuts import render

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
