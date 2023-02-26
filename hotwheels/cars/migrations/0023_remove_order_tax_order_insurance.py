# Generated by Django 4.1.4 on 2023-01-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0022_remove_taxandother_insu_nameid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tax',
        ),
        migrations.AddField(
            model_name='order',
            name='insurance',
            field=models.IntegerField(default=None, null=True, verbose_name='Insurance Amount'),
        ),
    ]