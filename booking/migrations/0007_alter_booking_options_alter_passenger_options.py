# Generated by Django 5.1.5 on 2025-02-15 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_passenger_data_birth'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='passenger',
            options={'managed': False},
        ),
    ]
