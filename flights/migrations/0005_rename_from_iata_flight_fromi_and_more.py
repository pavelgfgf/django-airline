# Generated by Django 5.1.5 on 2025-02-07 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_alter_flight_to_iata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='from_iata',
            new_name='fromi',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='to_iata',
            new_name='to',
        ),
    ]
