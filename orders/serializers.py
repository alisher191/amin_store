from rest_framework import serializers

from .models import Order, Delivery, Feedback


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'
