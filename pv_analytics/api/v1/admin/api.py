import functools
import operator

from rest_framework import viewsets, generics, views, mixins, status
from rest_framework.response import Response

from django.db.models import Max, Q

from pv_analytics.api.v1.admin.utils import calculate_balance
from pv_analytics.apps.users.permissions import (
    IsAuthenticated,
    IsAdmin,
)
from pv_analytics.utils.api_filters import (
    MeterP30DataFilter,
    BalancesFilter,
)
from pv_analytics.utils.mixins import ViewSetPagination
from pv_analytics.apps.initial_pv_data.models import (
    MeterP30Data,
    Balance,
    Sites,
)
from pv_analytics.apps.corrected_pv_data.models import CorrectedMeterP30Data
from pv_analytics.api.v1.admin.serializers import (
    MeterP30DataModelSerializer,
    CorrectedMeterP30DataModelSerializer,
    BalanceModelSerializer,
)


class MeterP30DataViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API for getting list of initial meter p30 data
    """

    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = MeterP30DataModelSerializer
    pagination_class = ViewSetPagination
    queryset = MeterP30Data.objects.using("remote").select_related("meter").all().order_by("-id")
    filterset_class = MeterP30DataFilter


class CorrectedMeterP30DataViewSet(viewsets.ModelViewSet):
    """
    API for performing CRUD operations under corrected data
    """

    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = CorrectedMeterP30DataModelSerializer
    queryset = CorrectedMeterP30Data.objects.all()

    def destroy(self, request, *args, **kwargs):
        """
        If corrected data deletes, then we should recalculate balance again
        for meter p30 data
        """
        instance = self.get_object()
        corrected_meter_p30_data_values = instance.values
        meter_p30_data_id = instance.meter_data_id
        self.perform_destroy(instance)
        calculate_balance(meter_p30_data_id, corrected_meter_p30_data_values)

        return Response(status=status.HTTP_204_NO_CONTENT)


class CorrectedDataByMeterId(generics.ListAPIView):
    """
    API for getting list of corrected data by meter ID
    """

    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = CorrectedMeterP30DataModelSerializer

    def get_queryset(self):
        return CorrectedMeterP30Data.objects.filter(meter_data_id=self.kwargs["meter_data_id"])


class BalancesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API for getting list of balances for sites
    Each site and date columns should be unique
    If there are many similar records with different versions,
    then get record with the largest version
    """

    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = BalanceModelSerializer
    filterset_class = BalancesFilter

    def get_queryset(self):
        # If no sites passed in query_params - then just return empty list
        sites = self.request.query_params.getlist("site")
        if all("" == s or s.isspace() for s in sites):
            return Balance.objects.using("remote").none()

        # Query record with largest version in group (By Site and date)
        group_by_expression = Balance.objects.using("remote").values("site", "date").annotate(version=Max("version"))
        filter_qry = functools.reduce(operator.or_, [Q(**item) for item in group_by_expression])
        qs = Balance.objects.using("remote").filter(filter_qry)
        return qs


class SitesListViewSet(views.APIView):
    """
    API for getting list of site names
    """

    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request, *args, **kwargs):
        queryset = Sites.objects.using("remote").all().values_list("displayable_name", flat=True)
        return Response(data=queryset)
