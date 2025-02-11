from django.db import models
from airport.models import Airport

# Create your models here.
class Flight(models.Model):
    flight = models.CharField(max_length=10)
    fromi = models.ForeignKey(Airport,related_name='departures', on_delete=models.CASCADE)
    to = models.ForeignKey(Airport,related_name='arrivals', on_delete=models.CASCADE)
    date_1 = models.DateField()
    date_2 = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=1)
    availability = models.IntegerField() 


    def __str__(self):
         return f"{self.flight}: {self.fromi.iata} → {self.to.iata}" 