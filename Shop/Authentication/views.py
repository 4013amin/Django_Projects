from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from . import models
from .serializers import RegisterSerializer


# Create your views here.
@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')

        if models.User.objects.filter(username=username).exists():
            return Response({'error': 'این نام کاربری قبلاً استفاده شده است.'}, status=status.HTTP_400_BAD_REQUEST)

        # ایجاد کاربر
        user = models.User.objects.create_user(
            username=username,
            password=serializer.validated_data.get('password'),
            email=serializer.validated_data.get('email')
        )
        user.save()

        # ایجاد پروفایل
        models.ProfileApi.objects.create(
            user=user,
            credit=serializer.validated_data.get('credit'),
            image=request.FILES.get('image')
        )

        return Response({'success': 'ثبت‌نام با موفقیت انجام شد.'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = request.user.username

        if not username:
            return Response({"error": "کاربر یافت نشد."}, status=status.HTTP_404_NOT_FOUND)

        # دریافت پروفایل کاربر
        try:
            profile = models.ProfileApi.objects.get(user__username=username)
            serializer = RegisterSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except models.ProfileApi.DoesNotExist:
            return Response({"error": "پروفایل یافت نشد."}, status=status.HTTP_404_NOT_FOUND)
