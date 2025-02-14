from django.db import models
from flights.models import Flight

# Create your models here.        
class Booking(models.Model):
    booking_number = models.CharField(max_length=255, null=True, blank=True)
    flight = models.ForeignKey(Flight, related_name='booking_flight', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.booking_number or ''

class Passenger(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    data_birth = models.DateField(null=True, blank=True)
    document_number = models.CharField(max_length=128)
    booking = models.ForeignKey(Booking, related_name='passenger_booking', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.first_name