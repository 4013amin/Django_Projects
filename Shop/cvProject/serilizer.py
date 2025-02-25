from rest_framework import serializers
from . import models


class AddUsers(serializers.ModelSerializer):
    class Meta:
        model = models.Concert
        fields = '__all__'
