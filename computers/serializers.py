from rest_framework import serializers

from . import models
from orders.seraializers import FeedbackSerializer


class ProductSerializers(serializers.ModelSerializer):
    feedback = FeedbackSerializer(many=True)
    class Meta:
        model = models.Product
        fields = '__all__'


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Computer
        fields = '__all__'
