import django_filters
from .models import Computer, Product

class ComputerFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    brand = django_filters.CharFilter(lookup_expr='exact')
    model = django_filters.CharFilter(lookup_expr='exact')
    price = django_filters.RangeFilter()
    sale = django_filters.NumberFilter()
    is_game = django_filters.BooleanFilter()
    year = django_filters.NumberFilter()
    active = django_filters.BooleanFilter()
    product_id = django_filters.NumberFilter(field_name='cpu_id')

    class Meta:
        model = Computer
        fields = ['title', 'description', 'brand', 'model', 'price', 'sale', 'is_game', 'year', 'active', 'product_id']


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    sub_title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    brand = django_filters.CharFilter(lookup_expr='exact')
    model = django_filters.CharFilter(lookup_expr='exact')
    price = django_filters.RangeFilter()
    sale = django_filters.CharFilter(lookup_expr='exact')
    category = django_filters.CharFilter(lookup_expr='exact')
    year = django_filters.NumberFilter()
    active = django_filters.BooleanFilter()

    class Meta:
        model = Product
        fields = ['title', 'sub_title', 'description', 'brand', 'model', 'price', 'sale', 'category', 'year', 'active']
