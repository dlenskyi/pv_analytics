from django.db.models import Q
from django_filters import rest_framework as filters


class MeterP30DataFilter(filters.FilterSet):
    date_start = filters.CharFilter(
        field_name='date', lookup_expr='gte'
    )
    date_end = filters.CharFilter(field_name='date', lookup_expr='lte')
    device = filters.CharFilter(method='device_filter')
    site = filters.CharFilter(method='site_filter')

    def site_filter(self, queryset, name, value):
        # Since we get multiple site names in query_params, we need to filter
        # all sites that are in this list
        sites = self.request.query_params.getlist('site')
        return queryset.using('remote').filter(
            meter__site__displayable_name__in=sites
        )

    def device_filter(self, queryset, name, value):
        return queryset.using('remote').filter(
            Q(meter__name__icontains=value) | Q(meter__id__icontains=value)
        )


class BalancesFilter(filters.FilterSet):
    date_start = filters.CharFilter(
        field_name='date', lookup_expr='gte'
    )
    date_end = filters.CharFilter(field_name='date', lookup_expr='lte')
    site = filters.CharFilter(method='site_filter')

    def site_filter(self, queryset, name, value):
        # Since we get multiple site names in query_params, we need to filter
        # all sites that are in this list
        sites = self.request.query_params.getlist('site')
        return queryset.using('remote').filter(
            site__displayable_name__in=sites
        )
