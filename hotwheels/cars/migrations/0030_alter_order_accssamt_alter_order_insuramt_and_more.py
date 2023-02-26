# Generated by Django 4.1.4 on 2023-02-08 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0029_order_accssamt_order_insuramt_order_regst_amt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='accssamt',
            field=models.FloatField(default=None, null=True, verbose_name='Accessories Total'),
        ),
        migrations.AlterField(
            model_name='order',
            name='insuramt',
            field=models.FloatField(default=None, null=True, verbose_name='Insurance Amount'),
        ),
        migrations.AlterField(
            model_name='order',
            name='regst_amt',
            field=models.FloatField(default=None, null=True, verbose_name='Registration Amount'),
        ),
        migrations.AlterField(
            model_name='order',
            name='road_tax',
            field=models.FloatField(default=None, null=True, verbose_name='Road Tax'),
        ),
    ]
