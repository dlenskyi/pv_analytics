# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Balance(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=250)
    site = models.ForeignKey('Sites', models.DO_NOTHING, db_column='site')
    date = models.DateField()
    time_indexes_utc = ArrayField(
        models.DateTimeField(),
        blank=True
    )
    energy = ArrayField(
        models.IntegerField(),
        blank=True
    )
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'balance'


class Equipment(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=250)
    name = models.CharField(max_length=20)
    data_header = models.TextField(blank=True, null=True)  # This field type is a guess.
    site_id = models.IntegerField()
    is_border = models.BooleanField(blank=True, null=True)
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'equipment'


class ForecastLogbook(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=250)
    supplier = models.CharField(max_length=15, blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    issued_utc = models.DateTimeField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    file_name = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forecast_logbook'


class ForecastsApplied(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=250)
    site = models.ForeignKey('Sites', models.DO_NOTHING, db_column='site')
    date = models.DateField()
    time_indexes_utc = ArrayField(
        models.DateTimeField(),
        blank=True
    )
    energy = ArrayField(
        models.IntegerField(),
        blank=True
    )
    is_initial = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'forecasts_applied'


class InverterData(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=250)
    device_id = models.CharField(max_length=25)
    timestamp_utc = models.DateTimeField()
    t_inside = models.FloatField(blank=True, null=True)
    u_ac_1 = models.FloatField(blank=True, null=True)
    u_ac_2 = models.FloatField(blank=True, null=True)
    u_ac_3 = models.FloatField(blank=True, null=True)
    i_ac_1 = models.FloatField(blank=True, null=True)
    i_ac_2 = models.FloatField(blank=True, null=True)
    i_ac_3 = models.FloatField(blank=True, null=True)
    p_ac = models.FloatField(blank=True, null=True)
    q_ac = models.FloatField(blank=True, null=True)
    cosphi = models.FloatField(blank=True, null=True)
    frequency = models.FloatField(blank=True, null=True)
    u_dc = models.FloatField(blank=True, null=True)
    i_dc = models.FloatField(blank=True, null=True)
    i_dc_1 = models.FloatField(blank=True, null=True)
    i_dc_2 = models.FloatField(blank=True, null=True)
    i_dc_3 = models.FloatField(blank=True, null=True)
    i_dc_4 = models.FloatField(blank=True, null=True)
    i_dc_5 = models.FloatField(blank=True, null=True)
    i_dc_6 = models.FloatField(blank=True, null=True)
    i_dc_7 = models.FloatField(blank=True, null=True)
    i_dc_8 = models.FloatField(blank=True, null=True)
    i_dc_9 = models.FloatField(blank=True, null=True)
    p_dc = models.FloatField(blank=True, null=True)
    up_to_energy = models.FloatField(blank=True, null=True)
    iso_resistance = models.FloatField(blank=True, null=True)
    total_energy = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inverter_data'


class InverterDataTest(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=250)
    device_id = models.CharField(max_length=25)
    timestamp_utc = models.DateTimeField()
    t_inside = models.FloatField(blank=True, null=True)
    u_ac_1 = models.FloatField(blank=True, null=True)
    u_ac_2 = models.FloatField(blank=True, null=True)
    u_ac_3 = models.FloatField(blank=True, null=True)
    i_ac_1 = models.FloatField(blank=True, null=True)
    i_ac_2 = models.FloatField(blank=True, null=True)
    i_ac_3 = models.FloatField(blank=True, null=True)
    p_ac = models.FloatField(blank=True, null=True)
    q_ac = models.FloatField(blank=True, null=True)
    cosphi = models.FloatField(blank=True, null=True)
    frequency = models.FloatField(blank=True, null=True)
    u_dc = models.FloatField(blank=True, null=True)
    i_dc = models.FloatField(blank=True, null=True)
    i_dc_1 = models.FloatField(blank=True, null=True)
    i_dc_2 = models.FloatField(blank=True, null=True)
    i_dc_3 = models.FloatField(blank=True, null=True)
    i_dc_4 = models.FloatField(blank=True, null=True)
    i_dc_5 = models.FloatField(blank=True, null=True)
    i_dc_6 = models.FloatField(blank=True, null=True)
    i_dc_7 = models.FloatField(blank=True, null=True)
    i_dc_8 = models.FloatField(blank=True, null=True)
    i_dc_9 = models.FloatField(blank=True, null=True)
    p_dc = models.FloatField(blank=True, null=True)
    up_to_energy = models.FloatField(blank=True, null=True)
    iso_resistance = models.FloatField(blank=True, null=True)
    total_energy = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inverter_data_test'


class LegalEntities(models.Model):
    full_name = models.CharField(max_length=70, blank=True, null=True)
    short_name = models.CharField(max_length=20, blank=True, null=True)
    edrpou = models.CharField(max_length=8)
    x_code = models.CharField(db_column='x-code', max_length=16, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'legal_entities'


class MeterP30Data(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=250)
    meter = models.ForeignKey('Meters', models.DO_NOTHING, db_column='meter')
    date = models.DateField()
    day_total = models.IntegerField(blank=True, null=True)
    number_1 = models.IntegerField(db_column='1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.IntegerField(db_column='2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.IntegerField(db_column='3', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.IntegerField(db_column='4', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5 = models.IntegerField(db_column='5', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_6 = models.IntegerField(db_column='6', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_7 = models.IntegerField(db_column='7', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_8 = models.IntegerField(db_column='8', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_9 = models.IntegerField(db_column='9', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_10 = models.IntegerField(db_column='10', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_11 = models.IntegerField(db_column='11', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_12 = models.IntegerField(db_column='12', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_13 = models.IntegerField(db_column='13', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_14 = models.IntegerField(db_column='14', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_15 = models.IntegerField(db_column='15', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_16 = models.IntegerField(db_column='16', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_17 = models.IntegerField(db_column='17', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_18 = models.IntegerField(db_column='18', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_19 = models.IntegerField(db_column='19', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20 = models.IntegerField(db_column='20', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_21 = models.IntegerField(db_column='21', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_22 = models.IntegerField(db_column='22', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_23 = models.IntegerField(db_column='23', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_24 = models.IntegerField(db_column='24', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_25 = models.IntegerField(db_column='25', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_26 = models.IntegerField(db_column='26', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_27 = models.IntegerField(db_column='27', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_28 = models.IntegerField(db_column='28', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_29 = models.IntegerField(db_column='29', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_30 = models.IntegerField(db_column='30', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_31 = models.IntegerField(db_column='31', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_32 = models.IntegerField(db_column='32', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_33 = models.IntegerField(db_column='33', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_34 = models.IntegerField(db_column='34', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_35 = models.IntegerField(db_column='35', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_36 = models.IntegerField(db_column='36', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_37 = models.IntegerField(db_column='37', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_38 = models.IntegerField(db_column='38', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_39 = models.IntegerField(db_column='39', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_40 = models.IntegerField(db_column='40', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_41 = models.IntegerField(db_column='41', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_42 = models.IntegerField(db_column='42', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_43 = models.IntegerField(db_column='43', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_44 = models.IntegerField(db_column='44', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_45 = models.IntegerField(db_column='45', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_46 = models.IntegerField(db_column='46', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_47 = models.IntegerField(db_column='47', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_48 = models.IntegerField(db_column='48', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_49 = models.IntegerField(db_column='49', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_50 = models.IntegerField(db_column='50', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'meter_p30_data'


class Meters(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=250)
    name = models.CharField(max_length=50)
    site = models.ForeignKey('Sites', models.DO_NOTHING, db_column='site', blank=True, null=True)
    is_border = models.BooleanField()
    z_code = models.CharField(max_length=20, blank=True, null=True)
    serial_number = models.CharField(max_length=30, blank=True, null=True)
    parameter = models.CharField(max_length=2, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meters'


class SatecData(models.Model):
    timestamp_utc = models.DateTimeField()
    cosphi_1 = models.FloatField(blank=True, null=True)
    cosphi_2 = models.FloatField(blank=True, null=True)
    cosphi_3 = models.FloatField(blank=True, null=True)
    frequency = models.FloatField(blank=True, null=True)
    i_1 = models.FloatField(blank=True, null=True)
    i_2 = models.FloatField(blank=True, null=True)
    i_3 = models.FloatField(blank=True, null=True)
    u_1 = models.FloatField(blank=True, null=True)
    u_2 = models.FloatField(blank=True, null=True)
    u_3 = models.FloatField(blank=True, null=True)
    p_1 = models.FloatField(blank=True, null=True)
    p_2 = models.FloatField(blank=True, null=True)
    p_3 = models.FloatField(blank=True, null=True)
    p_total = models.FloatField(blank=True, null=True)
    q_1 = models.FloatField(blank=True, null=True)
    q_2 = models.FloatField(blank=True, null=True)
    q_3 = models.FloatField(blank=True, null=True)
    q_total = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'satec_data'


class SatecHourlyData(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=250)
    timestamp_utc = models.DateTimeField()
    cosphi_1 = models.FloatField(blank=True, null=True)
    cosphi_2 = models.FloatField(blank=True, null=True)
    cosphi_3 = models.FloatField(blank=True, null=True)
    frequency = models.FloatField(blank=True, null=True)
    i_1 = models.FloatField(blank=True, null=True)
    i_2 = models.FloatField(blank=True, null=True)
    i_3 = models.FloatField(blank=True, null=True)
    u_1 = models.FloatField(blank=True, null=True)
    u_2 = models.FloatField(blank=True, null=True)
    u_3 = models.FloatField(blank=True, null=True)
    p_1 = models.FloatField(blank=True, null=True)
    p_2 = models.FloatField(blank=True, null=True)
    p_3 = models.FloatField(blank=True, null=True)
    p_total = models.FloatField(blank=True, null=True)
    q_1 = models.FloatField(blank=True, null=True)
    q_2 = models.FloatField(blank=True, null=True)
    q_3 = models.FloatField(blank=True, null=True)
    q_total = models.FloatField(blank=True, null=True)
    device_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'satec_hourly_data'


class Sites(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=250)
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    location = models.TextField()  # This field type is a guess.
    legal_entity = models.IntegerField()
    region = models.CharField(max_length=20, blank=True, null=True)
    installed_capacity_dc = models.IntegerField(blank=True, null=True)
    installed_capacity_ac = models.IntegerField(blank=True, null=True)
    displayable_name = models.CharField(max_length=20, blank=True, null=True)
    w_code = models.CharField(db_column='w-code', max_length=16, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cells_area = models.IntegerField(blank=True, null=True)
    modules_area = models.IntegerField(blank=True, null=True)
    gpee_code = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sites'


class WeatherData(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=250)
    device_id = models.CharField(max_length=20)
    timestamp_utc = models.DateTimeField()
    ambient_temperature = models.FloatField(blank=True, null=True)
    module_temperature = models.FloatField(blank=True, null=True)
    irradiance_hor = models.FloatField(blank=True, null=True)
    irradiance_poa = models.FloatField(blank=True, null=True)
    wind_vel = models.FloatField(blank=True, null=True)
    wind_dir = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_data'


class WeatherHourlyData(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=250)
    device_id = models.CharField(max_length=20)
    timestamp_utc = models.DateTimeField()
    ambient_temperature = models.FloatField(blank=True, null=True)
    module_temperature = models.FloatField(blank=True, null=True)
    irradiance_hor = models.FloatField(blank=True, null=True)
    irradiance_poa = models.FloatField(blank=True, null=True)
    wind_vel = models.FloatField(blank=True, null=True)
    wind_dir = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_hourly_data'
