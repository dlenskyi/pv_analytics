from rest_framework import viewsets, mixins, generics

from pv_analytics.apps.users.permissions import (
    IsAuthenticated,
    IsAdmin,
)
from pv_analytics.utils.api_filters import MeterP30DataFilter
from pv_analytics.utils.mixins import ViewSetPagination
from pv_analytics.apps.initial_pv_data.models import MeterP30Data
from pv_analytics.apps.corrected_pv_data.models import CorrectedMeterP30Data
from pv_analytics.api.v1.admin.serializers import (
    MeterP30DataModelSerializer,
    CorrectedMeterP30DataModelSerializer,
)


class MeterP30DataViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]
    serializer_class = MeterP30DataModelSerializer
    pagination_class = ViewSetPagination
    queryset = MeterP30Data.objects.using('remote').select_related('meter').all().order_by('-id')
    filterset_class = MeterP30DataFilter


class CorrectedMeterP30DataViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]
    serializer_class = CorrectedMeterP30DataModelSerializer
    queryset = CorrectedMeterP30Data.objects.all()


class CorrectedDataByMeterId(
    generics.ListAPIView
):
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]
    serializer_class = CorrectedMeterP30DataModelSerializer

    def get_queryset(self):
        return CorrectedMeterP30Data.objects.filter(
            meter_data_id=self.kwargs['meter_data_id']
        )
