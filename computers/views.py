from django.shortcuts import render

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import AccessoriesCategory, Brand, Computer
from .serializers import AccesoriesSerializer, BrandSerializers, ComputerSerializer
from .permissions import  IsAdminOrReadOnly  # IsOwnerOrReadOnly,


#################################### Accessories #############################################


class AccesoriesCreate(CreateAPIView):
    queryset = AccessoriesCategory.objects.all()
    serializer_class = AccesoriesSerializer
    permission_classes = [IsAuthenticated]


class AccessoriesReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = AccessoriesCategory.objects.all()
    serializer_class = AccesoriesSerializer
    permission_classes = [IsAdminOrReadOnly]


class AccessoriesList(ListAPIView):
    queryset = AccessoriesCategory.objects.all()
    serializer_class = AccesoriesSerializer
    permission_classes = [IsAdminOrReadOnly]


####################################### Brands ###############################################


class BrandCreate(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
    permission_classes = [IsAuthenticated]


class BrandReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
    permission_classes = [IsAdminOrReadOnly]


class BrandsList(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
    permission_classes = [IsAdminOrReadOnly]


####################################### Computers #############################################


class ComputerCreate(CreateAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    permission_classes = [IsAuthenticated]


class ComputerReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    permission_classes = [IsAdminOrReadOnly]


class ComputersList(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    permission_classes = [IsAdminOrReadOnly]
