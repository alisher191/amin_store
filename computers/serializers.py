from rest_framework import serializers

from .models import AccessoriesType, Computer


class AccesoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesType
        fields = ['name', 'price', 'category']
