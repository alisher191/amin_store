import django_filters
from .models import Order, Delivery

class OrderFilter(django_filters.FilterSet):
    fullName = django_filters.CharFilter(lookup_expr='icontains')
    createdAt = django_filters.DateFilter()
    city = django_filters.CharFilter(lookup_expr='icontains')
    phoneNumber = django_filters.CharFilter(lookup_expr='icontains')
    product = django_filters.NumberFilter(field_name='product__id')
    willBeDeliveredAt = django_filters.DateFilter()
    active = django_filters.BooleanFilter()

    class Meta:
        model = Order
        fields = ['fullName', 'createdAt', 'city', 'phoneNumber', 'product', 'willBeDeliveredAt', 'active']


class DeliveryFilter(django_filters.FilterSet):
    ordersFullName = django_filters.CharFilter(field_name='order__fullName', lookup_expr='icontains')
    publishedAt = django_filters.DateFilter(field_name='order__createdAt')
    city = django_filters.CharFilter(field_name='order__city', lookup_expr='icontains')
    phoneNumber = django_filters.CharFilter(field_name='order__phoneNumber', lookup_expr='icontains')
    product = django_filters.NumberFilter(field_name='order__product__id')
    active = django_filters.BooleanFilter()

    class Meta:
        model = Delivery
        fields = ['ordersFullName', 'publishedAt', 'city', 'phoneNumber', 'product', 'active']
