from rest_framework import serializers

from .models import AccessoriesCategory, Computer, Brand


class AccesoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesCategory
        fields = '__all__'
        # fields = [
        #     "image",
        #     "category",
        #     "model_name",
        #     "price",
        #     "socket",
        #     "cache",
        #     "cores",
        #     "processor_frequency",
        #     "tech_process",
        #     "core",
        #     "max_frequency",
        #     "brand_name"
        # ]


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
