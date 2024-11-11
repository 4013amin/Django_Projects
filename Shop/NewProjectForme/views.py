from django.http import JsonResponse
from django.shortcuts import render
from .models import Users
from rest_framework import status
from rest_framework.response import Response
from .seializer import UserSerializer


# Create your views here.

def addUsers(request):
    users = UserSerializer(request.data)
    if users.is_valid():
        user = users.save()
        return Response(users, status=status.HTTP_201_CREATED)
    else:
        return Response(users.errors, status=status.HTTP_400_BAD_REQUEST)


def getUsers(request):
    users = Users.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def login(request):
    serializer = UserSerializer(request.user)
    if serializer.is_valid():
        username = serializer.data.get('username')
        password = serializer.data.get('password')

        users = Users.objects.filter(username=username, password=password)
        if users is None:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.data, status=status.HTTP_200_OK)
