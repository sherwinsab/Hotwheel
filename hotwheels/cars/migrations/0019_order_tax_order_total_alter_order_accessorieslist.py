# Generated by Django 4.1.4 on 2023-01-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0018_alter_information_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.FloatField(default=None, null=True, verbose_name='Tax Total'),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=None, null=True, verbose_name='Sum Total Of Car'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Accessorieslist',
            field=models.TextField(default=None, null=True, verbose_name='Accessories Added'),
        ),
    ]
