from rest_framework import serializers
from . import models


class AminUserSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.UsersAmin
        fields = '__all__'
