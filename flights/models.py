from django.db import models
from airport.models import Airport

# Create your models here.
class Flight(models.Model):
    flight_code = models.CharField(max_length=10)
    from_field = models.ForeignKey(Airport, models.DO_NOTHING, db_column='from_id')  # Field renamed because it was a Python reserved word.
    to = models.ForeignKey(Airport, models.DO_NOTHING, related_name='flights_to_set')
    time_from = models.TimeField()
    time_to = models.TimeField()
    cost = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flights'