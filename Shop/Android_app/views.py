from django.shortcuts import render
from rest_framework import response, status
from rest_framework.response import Response

from . import models
from . import serializers


# Create your views here.
def Register(request):
    serialyzer = serializers.users_serializers(data=request.data)
    if serialyzer.is_valid():
        serialyzer.save()
    else:
        return Response(serialyzer.errors, status=status.HTTP_400_BAD_REQUEST)
