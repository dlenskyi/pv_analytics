# Generated by Django 3.1.3 on 2020-11-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorrectedMeterP30Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_data_id', models.IntegerField()),
                ('key', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'зкоректоване значення',
                'verbose_name_plural': 'Зкоректовані значення',
                'db_table': 'p30_corrections',
                'ordering': ['-id'],
            },
        ),
    ]
