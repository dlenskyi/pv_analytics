from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField


class CorrectedMeterP30Data(models.Model):
    meter_data_id = models.IntegerField()
    values = ArrayField(
        models.IntegerField(),
        blank=True
    )
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)

    class Meta:
        db_table = 'p30_corrections'
        verbose_name = _('зкоректоване значення')
        verbose_name_plural = _('Зкоректовані значення')
        ordering = ['-id']
