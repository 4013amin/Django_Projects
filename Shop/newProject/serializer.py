from rest_framework import serializers
from .models import newData, BannerData


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = newData
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerData
        fields = '__all__'
