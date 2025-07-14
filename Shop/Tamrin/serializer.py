from rest_framework import serializers
from . import models


class TaskAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tasks
        fields = '__all__'

