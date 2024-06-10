from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UsersSerializer, user_testSerializer
from .models import Users, user_test, Login_users
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError


@api_view(['POST'])
def create_user(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Testi
@api_view(["POST"])
def send_request(request):
    number1 = request.data.get('number1', 0)
    number2 = request.data.get('number2', 0)
    result = number1 + number2
    return Response({'result': result}, status=status.HTTP_200_OK)


# @api_view("POST")
# def create_users_new(request):
#     serializer = UsersSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view("GET")
# def get_data(request):
#     get_users = Users.objects.all()
#     serializer = UsersSerializer(get_users, many=True)
#     return Response(serializer.data)


@api_view(["GET"])
def get_all_users(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)


# get_by_id
@api_view(["GET"])
def get_user_by_id(request, pk):
    users = Users.objects.get(id=pk)
    serializer = UsersSerializer(users, many=False)
    return Response(serializer.data)


# update
@api_view(["POST"])
def update_user(request, pk):
    instance = Users.objects.get(pk=pk)
    serializer = UsersSerializer(instance=instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


# DELETE_ALL_USERS
@api_view(["DELETE"])
def delete_all_user(request):
    instance = Users.objects.all()
    instance.delete()
    return Response("All_users deleted")


# DELETE_BY_ID
@api_view(["DELETE"])
def delete_user_id(request, pk):
    instance = Users.objects.get(pk=pk)
    instance.delete()
    return Response("users deleted")


# form_users
def register_users(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        register = Login_users(username, name, password, password2)
        if register.is_valid():
            register.save()

            context = {
                'response': "عملیات با موفقیت ذخیره شد"
            }

            return render(request, 'home.html', context)
        else:
            return render(request, 'home.html', {'error': register.errors})


