from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models
from .serializers import RegisterSerializer


# Create your views here.
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')

        if models.User.objects.filter(username=username).exists():
            return Response({'error': 'این نام کاربری قبلاً استفاده شده است.'}, status=status.HTTP_400_BAD_REQUEST)

        user = models.User.objects.create_user(
            username=username,
            password=serializer.validated_data.get('password'),
            email=serializer.validated_data.get('email')
        )

        user.save()

        models.ProfileApi.objects.create(
            user=user,
            credit=serializer.validated_data.get('credit'),
            image=serializer.validated_data.get('image')
        )

        return Response({'success': 'ثبت‌نام با موفقیت انجام شد.'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    try:
        profile = models.ProfileApi.objects.get(user=request.user)
        serializer = RegisterSerializer(profile)
        return Response(serializer.data)
    except models.ProfileApi.DoesNotExist:
        return Response({'error': 'پروفایل پیدا نشد.'}, status=status.HTTP_404_NOT_FOUND)
