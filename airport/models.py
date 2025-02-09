from django.db import models

# Create your models here.
class Airport(models.Model):
    city = models.CharField(max_length=128)
    airport = models.CharField(max_length=128)
    iata = models.CharField(max_length=3, unique=True)
    data = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return super().__str__()
    