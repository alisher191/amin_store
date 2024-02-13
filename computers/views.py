from django.shortcuts import render

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from .models import AccessoriesCategory
from .serializers import AccesoriesSerializer


class AccesoriesCreate(CreateAPIView):
    queryset = AccessoriesCategory.objects.all()
    serializer_class = AccesoriesSerializer


class AccessoriesReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = AccessoriesCategory.objects.all()
    serializer_class = AccesoriesSerializer

class AccessoriesList(ListAPIView):
    queryset = AccessoriesCategory.objects.all()
    serializer_class = AccesoriesSerializer
