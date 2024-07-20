from sqlite3 import IntegrityError

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import RegisterProfileForm
from .serializer import UserSerializer
from .models import ProfileUser


# Create your views here.
@api_view(["POST"])
def sendRequest(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User has been sent successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def RegisterUser(request):
    if request.method == 'POST':
        profileForm = RegisterProfileForm(request.POST, request.FILES)
        if profileForm.is_valid():
            try:
                user = User.objects.create_user(username=profileForm.cleaned_data["username"],
                                                password=profileForm.cleaned_data["password"],
                                                email=profileForm.cleaned_data["email"])

                profile = ProfileUser(user=user, image=profileForm.cleaned_data["image"])
                profile.save()
                return render(request, 'FormHome.html')
            except IntegrityError:
                profileForm.add_error('username', 'این نام کاربری قبلاً استفاده شده است.')
                return render(request, 'FormHome.html', {'form': profileForm})
        else:
            return render(request, 'FormHome.html', {'form': profileForm})
    else:
        profileForm = RegisterProfileForm()
        return render(request, 'FormHome.html', {'form': profileForm})


