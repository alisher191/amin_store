from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView
import django_filters

from computers.permissions import IsAdminOrReadOnly
from .filters import OrderFilter, DeliveryFilter
from .models import Order, Delivery, Feedback
from .seraializers import OrderSerializer, DeliverySerializer, FeedbackSerializer


############################################### Order #################################################

class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = OrderFilter
    pagination_class = LimitOffsetPagination
    ordering_fields = ['PUBLISHED_AT', 'importance']
    search_fields = ['city', 'street', 'product__title', 'product__sub_title', 'fullName']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Применение сортировки
        sort_by = self.request.query_params.get('sort[sortBy]')
        sort_direction = self.request.query_params.get('sort[sortDirection]')
        if sort_by and sort_direction:
            queryset = queryset.order_by(f'{sort_direction.lower()}{sort_by}')

        return queryset


class OrderCreaete(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrReadOnly]


class OrderReDelete(RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrReadOnly]

############################################### Delivery #################################################

class DeliveryList(ListAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = DeliveryFilter
    pagination_class = LimitOffsetPagination
    ordering_fields = ['order__PUBLISHED_AT', 'order__importance']
    search_fields = ['order__city', 'order__street', 'order__product__title', 'order__product__sub_title', 'order__fullName']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Применение сортировки
        sort_by = self.request.query_params.get('sort[sortBy]')
        sort_direction = self.request.query_params.get('sort[sortDirection]')
        if sort_by and sort_direction:
            queryset = queryset.order_by(f'order__{sort_direction.lower()}{sort_by}')

        return queryset


class DeliveryCreate(CreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAdminOrReadOnly]


class DeliveryReDelete(RetrieveDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAdminOrReadOnly]


############################################### Feedback #################################################


class FeedbackCreate(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackList(ListAPIView):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Feedback.objects.filter(product_id=product_id)


