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


# update
@api_view(["POST"])
def update_user(request, pk):
    instance = Users.objects.get(pk=pk)
    serializer = UsersSerializer(instance=instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


# DELETE
@api_view(["DELETE"])
def delete_user(request, pk):
    instance = Users.objects.get(pk=pk)
    instance.delete()
    return Response("users deleted")
