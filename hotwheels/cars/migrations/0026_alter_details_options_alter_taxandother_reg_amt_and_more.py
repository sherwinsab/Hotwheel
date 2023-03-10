# Generated by Django 4.1.4 on 2023-01-19 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0025_remove_taxandother_insurance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='details',
            options={'verbose_name': 'Vechile Information', 'verbose_name_plural': 'Car Details'},
        ),
        migrations.AlterField(
            model_name='taxandother',
            name='Reg_amt',
            field=models.FloatField(verbose_name='Registration Amount In Percentage %'),
        ),
        migrations.AlterField(
            model_name='taxandother',
            name='Road_tax',
            field=models.FloatField(verbose_name='Road tax Amount In Percentage %'),
        ),
    ]
