from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import users
from .serializers import usersSerializer, LoginSerializer
from django.core.files.storage import default_storage


# Create your views here.
@api_view(["POST"])
def sendRegister(request):
    serializer = usersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def sendLogin(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        if users.objects.filter(username=username, password=password):
            # User is authenticated
            return Response({"message": "Login Successful"}, status=status.HTTP_200_OK)
        else:
            # Authentication failed
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

