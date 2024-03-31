from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UsersSerializer
from .models import Users


@api_view(['POST'])
def create_user(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
