from django.db.models import Q
from django_filters import rest_framework as filters


class MeterP30DataFilter(filters.FilterSet):
    date_start = filters.CharFilter(
        field_name='date', lookup_expr='gte'
    )
    date_end = filters.CharFilter(field_name='date', lookup_expr='lte')
    device = filters.CharFilter(method='device_filter')
    site = filters.CharFilter(field_name='meter__site__displayable_name', lookup_expr='icontains')

    def device_filter(self, queryset, name, value):
        return queryset.using('remote').filter(
            Q(meter__name__icontains=value) | Q(meter__id__icontains=value)
        )
