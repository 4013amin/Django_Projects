from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import AminUserSerializer
from . import models


# Create your views here.
@api_view(["POST"])
def saveUser(request):
    serializer = AminUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    serializer = AminUserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data.get("username")
        phone = serializer.data.get("phone")

        user = models.UsersAmin.objects.filter(username=username, phone=phone).first()
        if user is None:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def logout(request):
    serializer = AminUserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data.get("username")
        phone = serializer.data.get("phone")
        user = models.UsersAmin.objects.filter(username=username, phone=phone).first()
        if user is None:
            serializer.delete()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
