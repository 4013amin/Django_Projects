from rest_framework import serializers
from .models import ProfileUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ['username', 'password', 'phone']

