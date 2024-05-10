from rest_framework import serializers

from .models import Users, user_test


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class user_testSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_test
        fields = "__all__"
