# Generated by Django 5.1.5 on 2025-01-31 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='passengers',
            new_name='availability',
        ),
    ]
