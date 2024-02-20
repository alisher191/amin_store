import django_filters
from .models import Computer

class ComputerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    section = django_filters.CharFilter(lookup_expr='exact')
    cpu_id = django_filters.CharFilter(lookup_expr='exact', field_name='cpu__name')
    price = django_filters.RangeFilter()

    class Meta:
        model = Computer
        fields = ['name', 'description', 'section', 'cpu_id', 'price']
