from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import DataSerializer

from .models import newData, BannerData


# Create your views here.
@api_view(["GET"])
def getData(request):
    data = newData.objects.all()
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)
