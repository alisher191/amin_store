from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers
from .permissions import  IsAdminOrReadOnly


####################################### Brands ###############################################


class BrandCreate(CreateAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializers
    permission_classes = [IsAuthenticated]


class BrandReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializers
    permission_classes = [IsAdminOrReadOnly]


class BrandsList(ListAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializers
    permission_classes = [IsAdminOrReadOnly]


####################################### Computers #############################################


class ComputerCreate(CreateAPIView):
    queryset = models.Computer.objects.all()
    serializer_class = serializers.ComputerSerializer
    permission_classes = [IsAuthenticated]


class ComputerReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Computer.objects.all()
    serializer_class = serializers.ComputerSerializer
    permission_classes = [IsAdminOrReadOnly]


class ComputersList(ListAPIView):
    queryset = models.Computer.objects.all()
    serializer_class = serializers.ComputerSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### VideoCard #############################################


class VideoCardCreate(CreateAPIView):
    queryset = models.VideoCard.objects.all()
    serializer_class = serializers.VideoCardSerializer
    permission_classes = [IsAuthenticated]


class VideoCardReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.VideoCard.objects.all()
    serializer_class = serializers.VideoCardSerializer
    permission_classes = [IsAdminOrReadOnly]


class VideoCardList(ListAPIView):
    queryset = models.VideoCard.objects.all()
    serializer_class = serializers.VideoCardSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### CPU #############################################


class CpuCreate(CreateAPIView):
    queryset = models.Cpu.objects.all()
    serializer_class = serializers.CpuSerializer
    permission_classes = [IsAuthenticated]


class CpuCardReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Cpu.objects.all()
    serializer_class = serializers.CpuSerializer
    permission_classes = [IsAdminOrReadOnly]


class CpuCardList(ListAPIView):
    queryset = models.Cpu.objects.all()
    serializer_class = serializers.CpuSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### Cooler #############################################


class CoolerCreate(CreateAPIView):
    queryset = models.Cooler.objects.all()
    serializer_class = serializers.CoolerSerializer
    permission_classes = [IsAuthenticated]


class CoolerReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Cooler.objects.all()
    serializer_class = serializers.CoolerSerializer
    permission_classes = [IsAdminOrReadOnly]


class CoolerList(ListAPIView):
    queryset = models.Cooler.objects.all()
    serializer_class = serializers.CoolerSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### Ram #############################################


class RamCreate(CreateAPIView):
    queryset = models.Ram.objects.all()
    serializer_class = serializers.RamSerializer
    permission_classes = [IsAuthenticated]


class RamReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Ram.objects.all()
    serializer_class = serializers.RamSerializer
    permission_classes = [IsAdminOrReadOnly]


class RamdList(ListAPIView):
    queryset = models.Ram.objects.all()
    serializer_class = serializers.RamSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### Motherboard #############################################


class MotherboardCreate(CreateAPIView):
    queryset = models.Motherboard.objects.all()
    serializer_class = serializers.MotherboardSerializer
    permission_classes = [IsAuthenticated]


class MotherboardReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Motherboard.objects.all()
    serializer_class = serializers.MotherboardSerializer
    permission_classes = [IsAdminOrReadOnly]


class MotherboardList(ListAPIView):
    queryset = models.Motherboard.objects.all()
    serializer_class = serializers.MotherboardSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### Hard #############################################


class HardCreate(CreateAPIView):
    queryset = models.Hard.objects.all()
    serializer_class = serializers.HardSerializer
    permission_classes = [IsAuthenticated]


class HardReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Hard.objects.all()
    serializer_class = serializers.HardSerializer
    permission_classes = [IsAdminOrReadOnly]


class HardList(ListAPIView):
    queryset = models.Hard.objects.all()
    serializer_class = serializers.HardSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### Ssd #############################################


class SsdCreate(CreateAPIView):
    queryset = models.Ssd.objects.all()
    serializer_class = serializers.SsdSerializer
    permission_classes = [IsAuthenticated]


class SsdReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Ssd.objects.all()
    serializer_class = serializers.SsdSerializer
    permission_classes = [IsAdminOrReadOnly]


class SsdList(ListAPIView):
    queryset = models.Ssd.objects.all()
    serializer_class = serializers.SsdSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### DVDDrive #############################################


class DVDDriveCreate(CreateAPIView):
    queryset = models.DVDDrive.objects.all()
    serializer_class = serializers.DVDDriveSerializer
    permission_classes = [IsAuthenticated]


class DVDDriveReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.DVDDrive.objects.all()
    serializer_class = serializers.DVDDriveSerializer
    permission_classes = [IsAdminOrReadOnly]


class DVDDriveList(ListAPIView):
    queryset = models.DVDDrive.objects.all()
    serializer_class = serializers.DVDDriveSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### PowerUnit #############################################


class PowerUnitCreate(CreateAPIView):
    queryset = models.PowerUnit.objects.all()
    serializer_class = serializers.PowerUnitSerializer
    permission_classes = [IsAuthenticated]


class PowerUnitReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.PowerUnit.objects.all()
    serializer_class = serializers.PowerUnitSerializer
    permission_classes = [IsAdminOrReadOnly]


class PowerUnitList(ListAPIView):
    queryset = models.PowerUnit.objects.all()
    serializer_class = serializers.PowerUnitSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### Body #############################################


class BodyCreate(CreateAPIView):
    queryset = models.Body.objects.all()
    serializer_class = serializers.BodySerializer
    permission_classes = [IsAuthenticated]


class BodyReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Body.objects.all()
    serializer_class = serializers.BodySerializer
    permission_classes = [IsAdminOrReadOnly]


class BodyList(ListAPIView):
    queryset = models.Body.objects.all()
    serializer_class = serializers.BodySerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### WiFiAdapter #############################################


class WiFiAdapterCreate(CreateAPIView):
    queryset = models.WiFiAdapter.objects.all()
    serializer_class = serializers.WiFiAdapterSerializer
    permission_classes = [IsAuthenticated]


class WiFiAdapterReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.WiFiAdapter.objects.all()
    serializer_class = serializers.WiFiAdapterSerializer
    permission_classes = [IsAdminOrReadOnly]


class WiFiAdapterList(ListAPIView):
    queryset = models.WiFiAdapter.objects.all()
    serializer_class = serializers.WiFiAdapterSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### AudioCard #############################################


class AudioCardCreate(CreateAPIView):
    queryset = models.AudioCard.objects.all()
    serializer_class = serializers.AudioCardSerializer
    permission_classes = [IsAuthenticated]


class AudioCardReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.AudioCard.objects.all()
    serializer_class = serializers.AudioCardSerializer
    permission_classes = [IsAdminOrReadOnly]


class AudioCardList(ListAPIView):
    queryset = models.AudioCard.objects.all()
    serializer_class = serializers.AudioCardSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### OSystem #############################################


class OSystemCreate(CreateAPIView):
    queryset = models.OSystem.objects.all()
    serializer_class = serializers.OSystemSerializer
    permission_classes = [IsAuthenticated]


class OSystemReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.OSystem.objects.all()
    serializer_class = serializers.OSystemSerializer
    permission_classes = [IsAdminOrReadOnly]


class OSystemList(ListAPIView):
    queryset = models.OSystem.objects.all()
    serializer_class = serializers.OSystemSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### Mouse #############################################


class MouseCreate(CreateAPIView):
    queryset = models.Mouse.objects.all()
    serializer_class = serializers.MouseCardSerializer
    permission_classes = [IsAuthenticated]


class MouseReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Mouse.objects.all()
    serializer_class = serializers.MouseCardSerializer
    permission_classes = [IsAdminOrReadOnly]


class MouseList(ListAPIView):
    queryset = models.Mouse.objects.all()
    serializer_class = serializers.MouseCardSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### Keyboard #############################################


class KeyboardCreate(CreateAPIView):
    queryset = models.Keyboard.objects.all()
    serializer_class = serializers.KeyboardSerializer
    permission_classes = [IsAuthenticated]


class KeyboardReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Keyboard.objects.all()
    serializer_class = serializers.KeyboardSerializer
    permission_classes = [IsAdminOrReadOnly]


class KeyboardList(ListAPIView):
    queryset = models.Keyboard.objects.all()
    serializer_class = serializers.KeyboardSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### Screen #############################################


class ScreenCreate(CreateAPIView):
    queryset = models.Screen.objects.all()
    serializer_class = serializers.ScreenSerializer
    permission_classes = [IsAuthenticated]


class ScreenReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Screen.objects.all()
    serializer_class = serializers.ScreenSerializer
    permission_classes = [IsAdminOrReadOnly]


class ScreenList(ListAPIView):
    queryset = models.Screen.objects.all()
    serializer_class = serializers.ScreenSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### Headset #############################################


class HeadsetCreate(CreateAPIView):
    queryset = models.Headset.objects.all()
    serializer_class = serializers.HeadsetSerializer
    permission_classes = [IsAuthenticated]


class HeadsetReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Headset.objects.all()
    serializer_class = serializers.HeadsetSerializer
    permission_classes = [IsAdminOrReadOnly]


class HeadsetList(ListAPIView):
    queryset = models.Headset.objects.all()
    serializer_class = serializers.HeadsetSerializer
    permission_classes = [IsAdminOrReadOnly]
