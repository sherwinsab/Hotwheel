# Generated by Django 4.1.4 on 2023-01-12 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0024_alter_order_insurance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxandother',
            name='Insurance',
        ),
    ]