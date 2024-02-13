from django.shortcuts import render

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from .models import AccessoriesType
from .serializers import AccesoriesSerializer


class AccesoriesCreate(CreateAPIView):
    queryset = AccessoriesType.objects.all()
    serializer_class = AccesoriesSerializer


class AccessoriesReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = AccessoriesType.objects.all()
    serializer_class = AccesoriesSerializer

class AccessoriesList(ListAPIView):
    queryset = AccessoriesType.objects.all()
    serializer_class = AccesoriesSerializer
