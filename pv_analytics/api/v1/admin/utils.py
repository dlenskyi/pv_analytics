import re
from collections import OrderedDict
import datetime as dt
import pandas as pd

from django.db.models import Max

from pv_analytics.apps.initial_pv_data.models import (
    MeterP30Data,
    Balance,
)


def update_ordered_dict(old_dict):
    """
    Returns fresh OrderedDict
    with replaced fields 'number_*digit*' to '*digit*'
    """
    return OrderedDict(
        [(re.sub('\\D', '', k), v) if k.startswith('number_') else (k, v) for
         k, v in
         old_dict.items()]
    )


def get_utc_index(date):
    """
    Returns array of UTC datetimes with 1H frequency based on date
    """
    start = dt.datetime(year=date.year, month=date.month, day=date.day, hour=0, minute=30)
    end = dt.datetime(year=date.year, month=date.month, day=date.day + 1, hour=0, minute=30) - dt.timedelta(hours=1)
    index_in_kyiv = pd.date_range(start=start, end=end, freq='1H', tz='Europe/kiev')
    index_in_utc = index_in_kyiv.tz_convert('utc').tz_localize(None)
    return index_in_utc.to_pydatetime().tolist()


def calculate_balance(meter_p30_data_id, corrected_meter_p30_data_values):
    """
    Recalculates balance for paired meters
    and creates new Balance with fresh version.
    Based on new meter that have been updated with corrected data
    """
    try:
        first_meter_p30_data = MeterP30Data.objects.using('remote').get(
            id=meter_p30_data_id
        )
    except MeterP30Data.DoesNotExist:
        return
    if not first_meter_p30_data.meter.site:
        return

    parameters_for_balance = ('A+', 'A-')
    generation_parameter = 'A-'
    first_meter_inst = first_meter_p30_data.meter
    if first_meter_inst.parameter in parameters_for_balance:
        # Get meter with opposite param than initial_meter
        # (if first is A+, second will be A-, and vise versa)
        second_meter_p30_data = MeterP30Data.objects.using('remote').filter(
            meter__serial_number=first_meter_inst.serial_number,
            date=first_meter_p30_data.date,
            meter__parameter__in=parameters_for_balance
        ).exclude(
            meter__parameter=first_meter_inst.parameter
        ).first()

        # Sum pairs of meter values for first meter
        first_paired_values_sum = []
        it = iter(corrected_meter_p30_data_values)
        for val1, val2 in zip(it, it):
            first_paired_values_sum.append(val1 + val2)

        # Same for second meter
        second_paired_values_sum = []
        for meter_index in range(1, 50, 2):
            val1 = getattr(second_meter_p30_data, f'number_{meter_index}')
            val2 = getattr(second_meter_p30_data, f'number_{meter_index + 1}')
            second_paired_values_sum.append(val1 + val2)

        # Calculate balance for that meters
        # (subtracting consumption from generation (A- - A+))
        total_balance_values = []
        if first_meter_inst.parameter == generation_parameter:
            total_paired_values = zip(
                first_paired_values_sum,
                second_paired_values_sum
            )
        else:
            total_paired_values = zip(
                second_paired_values_sum,
                first_paired_values_sum
            )
        for generation, consumption in total_paired_values:
            total_balance_values.append(generation - consumption)

        # Get time indexes by that date
        time_indexes_utc = get_utc_index(first_meter_p30_data.date)

        # Delete last elements in balance values list *diff* times
        # so time indexes and balance lists will have equal length
        diff = abs(len(time_indexes_utc) - len(total_balance_values))
        for i in range(diff):
            del total_balance_values[-1]

        # Get last version of balance, and add to it +1,
        # or set it to 1 by default
        balance = Balance.objects.using('remote').filter(
            site=first_meter_inst.site,
            date=first_meter_p30_data.date
        ).aggregate(Max('version'))
        version = balance.get('version__max')
        if version:
            version += 1
        else:
            version = 1
        Balance.objects.using('remote').create(
            site=first_meter_inst.site,
            date=first_meter_p30_data.date,
            time_indexes_utc=time_indexes_utc,
            energy=total_balance_values,
            version=version
        )
