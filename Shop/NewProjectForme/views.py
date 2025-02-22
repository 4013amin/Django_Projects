from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import users
from .seializer import UserSerializer
from django.contrib.auth import authenticate

class AddUsersView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUsersView(APIView):
    def get(self, request):
        users = users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_400_BAD_REQUEST
            )


class DeleteView(APIView):
    def delete(self, request):
        user_id = request.data.get('id')
        
        if not user_id:
            return Response(
                {"error": "ID is required to delete a user."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            user = users.objects.get(id=user_id)
            
            user.delete()
            
            return Response(
                {"message": "User deleted successfully."},
                status=status.HTTP_204_NO_CONTENT
            )
        except users.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )


class save(APIView):
    def save(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class getUsers(APIView):
    def getUsers(self,request):
        users = User.objects.all()
        seializer = UserSerializer(users , many = True)
        return Response(seializer.data , status=status.HTTP_200_OK)
    