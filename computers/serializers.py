from rest_framework import serializers

from . import models


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = '__all__'


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Computer
        fields = '__all__'


class VideoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VideoCard
        fields = '__all__'


class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cpu
        fields = '__all__'


class CoolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cooler
        fields = '__all__'


class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ram
        fields = '__all__'


class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motherboard
        fields = '__all__'


class HardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hard
        fields = '__all__'


class SsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ssd
        fields = '__all__'


class DVDDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DVDDrive
        fields = '__all__'


class PowerUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PowerUnit
        fields = '__all__'


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Body
        fields = '__all__'


class WiFiAdapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WiFiAdapter
        fields = '__all__'


class AudioCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AudioCard
        fields = '__all__'


class OSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OSystem
        fields = '__all__'


class MouseCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mouse
        fields = '__all__'


class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Keyboard
        fields = '__all__'


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Screen
        fields = '__all__'


class HeadsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Headset
        fields = '__all__'
