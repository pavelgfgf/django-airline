from django.db import models
from flights.models import Flight

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    document_number = models.CharField(max_length=128)
    flight = models.ForeignKey(Flight, related_name='booking_flight', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.first_name