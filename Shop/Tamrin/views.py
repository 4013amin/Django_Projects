from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializer import UserSerializer


# Create your views here.
@api_view(["POST"])
def sendRequest(request):
    if request.method == "POST":
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response({"message": "User has been sent successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
