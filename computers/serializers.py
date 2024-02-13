from rest_framework import serializers

from .models import AccessoriesCategory, Computer


class AccesoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesCategory
        fields = ['name', 'price', 'category']
