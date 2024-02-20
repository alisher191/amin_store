from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, pagination
import django_filters

from . import models
from . import serializers
from .permissions import  IsAdminOrReadOnly
from .filters import ComputerFilter, ProductFilter


####################################### Product ###############################################


class ProductCreate(CreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
    permission_classes = [IsAuthenticated]


class ProductReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
    permission_classes = [IsAdminOrReadOnly]


class ProductList(ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = ProductFilter
    pagination_class = pagination.LimitOffsetPagination
    ordering_fields = ['powerScale', 'PUBLISHED_AT', 'importance', 'year']
    search_fields = ['title', 'sub_title', 'description', 'brand', 'model', 'category']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Применение сортировки
        sort_by = self.request.query_params.get('sort[sortBy]')
        sort_direction = self.request.query_params.get('sort[sortDirection]')
        if sort_by and sort_direction:
            queryset = queryset.order_by(f'{sort_direction.lower()}{sort_by}')

        return queryset


####################################### Computers #############################################


class ComputerCreate(CreateAPIView):
    queryset = models.Computer.objects.all()
    serializer_class = serializers.ComputerSerializer
    permission_classes = [IsAuthenticated]


class ComputerReUpDelete(RetrieveUpdateDestroyAPIView):
    queryset = models.Computer.objects.all()
    serializer_class = serializers.ComputerSerializer
    permission_classes = [IsAdminOrReadOnly]


class ComputerListView(ListAPIView):
    serializer_class = serializers.ComputerSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = ComputerFilter
    queryset = models.Computer.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'brand', 'model', 'category', 'cpu__title', 'videoCard__title']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Применение сортировки
        sort_by = self.request.query_params.get('sort[sortBy]')
        sort_direction = self.request.query_params.get('sort[sortDirection]')
        if sort_by and sort_direction:
            queryset = queryset.order_by(f'{sort_direction.lower()}{sort_by}')

        return queryset

