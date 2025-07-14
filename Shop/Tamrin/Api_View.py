from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from .serializer import TaskAddSerializer


class TastkViewSet(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TaskAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        tasks = models.Tasks.objects.all()
        serializer = TaskAddSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
