from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    return render(request, 'login_register.html')

def home_view(request):
    return HttpResponse("This is a dummy home page.")
