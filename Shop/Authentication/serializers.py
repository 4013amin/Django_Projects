from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class RegisterSerializer(serializers.ModelSerializer):
    credit = serializers.IntegerField()
    image = serializers.ImageField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'credit', 'image']
        extra_kwargs = {
            'password': {'write_only': True}
        }
