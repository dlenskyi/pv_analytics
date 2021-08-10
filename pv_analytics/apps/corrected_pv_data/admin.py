from django.contrib import admin
from .models import CorrectedMeterP30Data


class CorrectedMeterP30DataAdmin(admin.ModelAdmin):
    model = CorrectedMeterP30Data

    list_display = [
        "meter_data_id",
        "values",
        "message",
        "date",
    ]
    list_filter = ["meter_data_id", "date"]
    search_fields = [
        "meter_data_id",
    ]


admin.site.register(CorrectedMeterP30Data, CorrectedMeterP30DataAdmin)
