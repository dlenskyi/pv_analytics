import re
from collections import OrderedDict

from django.utils.translation import (
    gettext as _,
    gettext_lazy,
)

from rest_framework import serializers
from pv_analytics.apps.initial_pv_data.models import MeterP30Data
from pv_analytics.apps.corrected_pv_data.models import CorrectedMeterP30Data


def update_ordered_dict(old_dict):
    return OrderedDict(
        [(re.sub('\\D', '', k), v) if k.startswith('number_') else (k, v) for
         k, v in
         old_dict.items()]
    )


class MeterP30DataModelSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return update_ordered_dict(data)

    class Meta:
        model = MeterP30Data
        fields = '__all__'


class CorrectedMeterP30DataModelSerializer(serializers.ModelSerializer):
    message = serializers.CharField(required=True)
    meter_data_id = serializers.IntegerField(required=True)
    key = serializers.CharField(required=True)
    value = serializers.IntegerField(required=True)

    class Meta:
        model = CorrectedMeterP30Data
        fields = '__all__'
