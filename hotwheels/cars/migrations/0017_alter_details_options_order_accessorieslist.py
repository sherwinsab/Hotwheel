# Generated by Django 4.1.4 on 2023-01-07 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_rename_tax_and_other_taxandother'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='details',
            options={'verbose_name': 'Vechile Information', 'verbose_name_plural': 'CAR DETAILS'},
        ),
        migrations.AddField(
            model_name='order',
            name='Accessorieslist',
            field=models.TextField(default=None, null=True),
        ),
    ]
