# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airports(models.Model):
    id = models.BigAutoField(primary_key=True)
    city = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    iata = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airports'


class Bookings(models.Model):
    id = models.BigAutoField(primary_key=True)
    flight_from = models.ForeignKey('Flights', models.DO_NOTHING, db_column='flight_from')
    flight_back = models.ForeignKey('Flights', models.DO_NOTHING, db_column='flight_back', related_name='bookings_flight_back_set', blank=True, null=True)
    date_from = models.DateField()
    date_back = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=5)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookings'


class Flights(models.Model):
    id = models.BigAutoField(primary_key=True)
    flight_code = models.CharField(max_length=10)
    from_field = models.ForeignKey(Airports, models.DO_NOTHING, db_column='from_id')  # Field renamed because it was a Python reserved word.
    to = models.ForeignKey(Airports, models.DO_NOTHING, related_name='flights_to_set')
    time_from = models.TimeField()
    time_to = models.TimeField()
    cost = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flights'


class Passengers(models.Model):
    id = models.BigAutoField(primary_key=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    document_number = models.CharField(max_length=10)
    place_from = models.CharField(max_length=3, blank=True, null=True)
    place_back = models.CharField(max_length=3, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passengers'
