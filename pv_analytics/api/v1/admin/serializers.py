from django.utils.translation import (
    gettext as _,
    gettext_lazy,
)

from rest_framework import serializers

from pv_analytics.api.v1.admin.utils import (
    update_ordered_dict,
    calculate_balance,
)
from pv_analytics.apps.initial_pv_data.models import (
    MeterP30Data,
    Balance,
)
from pv_analytics.apps.corrected_pv_data.models import CorrectedMeterP30Data


class MeterP30DataModelSerializer(serializers.ModelSerializer):
    device_name = serializers.SerializerMethodField()
    site_name = serializers.SerializerMethodField()

    def get_device_name(self, obj):
        return obj.meter.name or obj.meter.id

    def get_site_name(self, obj):
        if obj.meter.site:
            return obj.meter.site.displayable_name

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return update_ordered_dict(data)

    class Meta:
        model = MeterP30Data
        exclude = ("meter",)


class CorrectedMeterP30DataModelSerializer(serializers.ModelSerializer):
    message = serializers.CharField()
    meter_data_id = serializers.IntegerField()
    values = serializers.ListField()

    def create(self, validated_data):
        instance = super().create(validated_data)
        # Create Balance with new version according to corrections
        corrected_meter_p30_data_values = instance.values
        meter_p30_data_id = instance.meter_data_id
        calculate_balance(meter_p30_data_id, corrected_meter_p30_data_values)

        return instance

    class Meta:
        model = CorrectedMeterP30Data
        fields = "__all__"


class BalanceModelSerializer(serializers.ModelSerializer):
    site = serializers.CharField(source="site.displayable_name")
    energy_installed_capacity_ac = serializers.SerializerMethodField()
    energy_installed_capacity_dc = serializers.SerializerMethodField()

    def get_energy_installed_capacity_ac(self, obj):
        """
        Get array of energy values divided by installed capacity AC of Site
        """
        return [energy / obj.site.installed_capacity_ac for energy in obj.energy]

    def get_energy_installed_capacity_dc(self, obj):
        """
        Get array of energy values divided by installed capacity DC of Site
        """
        return [energy / obj.site.installed_capacity_dc for energy in obj.energy]

    class Meta:
        model = Balance
        fields = "__all__"
