# Generated by Django 4.1.4 on 2022-12-28 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_delete_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, default=None, max_length=1200, null=True, verbose_name='Description Of The Vehicle')),
                ('general_information', models.CharField(blank=True, default=None, max_length=1200, null=True, verbose_name='General Information Of The Vehicle')),
                ('vehicle_overview', models.CharField(blank=True, default=None, max_length=1200, null=True, verbose_name='Vehicle overview')),
                ('tax_amount', models.IntegerField(verbose_name='Tax Amount Of Car')),
                ('delivery_days', models.IntegerField(verbose_name='Delivery Days Of Car')),
                ('delivery_cost', models.IntegerField(verbose_name='Delivery Cost Of The car')),
                ('booking_amount', models.IntegerField(verbose_name='Booking Amount')),
                ('carnameid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.details', verbose_name='Car Name')),
                ('companyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.company', verbose_name='Car Company')),
                ('typeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.type', verbose_name='Car Type')),
            ],
            options={
                'db_table': 'INFORMATION OF CARS',
            },
        ),
    ]
