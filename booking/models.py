from django.db import models

from flights.models import Flight


# Create your models here.        
class Booking(models.Model):
    flight_from = models.ForeignKey(Flight, models.DO_NOTHING, db_column='flight_from')
    flight_back = models.ForeignKey(Flight, models.DO_NOTHING, db_column='flight_back', related_name='bookings_flight_back_set', blank=True, null=True)
    date_from = models.DateField()
    date_back = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=5)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookings'


class Passenger(models.Model):
    booking = models.ForeignKey(Booking, models.DO_NOTHING)
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