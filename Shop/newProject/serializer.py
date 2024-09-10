from rest_framework import serializers
from .models import newData


class NewDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = newData
        fields = '__all__'
