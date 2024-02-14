from django.shortcuts import render

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import AccessoriesCategory, Brand
from .serializers import AccesoriesSerializer, BrandSerializers
from .permissions import  IsAdminOrReadOnly  # IsOwnerOrReadOnly,


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
