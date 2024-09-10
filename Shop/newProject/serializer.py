from rest_framework import serializers
from .models import newData


class NewDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = newData
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': False}  # فیلد name دیگر اجباری نیست
        }
