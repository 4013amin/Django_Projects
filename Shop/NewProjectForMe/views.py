from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status
from .serializer import DataSerializer
from . import models


@api_view(['POST'])
def sendData(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getData(request):
    data = models.Data.objects.all()
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)
