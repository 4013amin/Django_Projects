from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import newData

from .serializer import NewDataSerializer


# Create your views here.


@api_view(["POST"])
def sendNewData(request):
    serializer = NewDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)  # نمایش خطاهای اعتبارسنجی
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getAllNewData(request):
    data = newData.objects.all()
    serializer = NewDataSerializer(data, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteNewData(request, pk):
    data = newData.objects.get(pk=pk)
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["PUT"])
def updateData(request, pk):
    data = newData.objects.get(pk=pk)
    serializer = NewDataSerializer(data, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
