# Generated by Django 4.1.4 on 2023-01-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0023_remove_order_tax_order_insurance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='insurance',
            field=models.TextField(default=None, null=True, verbose_name='Insurance Amount'),
        ),
    ]
