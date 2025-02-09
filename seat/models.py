from django.db import models

# Create your models here.
class Seat(models.Model):
    passenger_id = models.IntegerField()
    place = models.CharField(max_length=5)


    def __str__(self):
        return self.passenger_id