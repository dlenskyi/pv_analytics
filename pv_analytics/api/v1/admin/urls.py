from django.urls import path
from rest_framework import routers
from .api import (
    MeterP30DataViewSet,
    CorrectedMeterP30DataViewSet,
    CorrectedDataByMeterId,
)


router = routers.DefaultRouter()

# Routes for CRUD operations under project apps
router.register('meter_p30_data', MeterP30DataViewSet, basename='meter-p30-data'),
router.register('corrected_meter_data', CorrectedMeterP30DataViewSet, basename='corrected-p30-data'),

urlpatterns = [
    path(
        'corrected_data_by_meter/<int:meter_data_id>/',
        CorrectedDataByMeterId.as_view(),
        name='corrected-data-by-meter',
    ),
] + router.urls  # adding routes to urls
