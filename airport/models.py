from django.db import models

# Create your models here.
class Airport(models.Model):
    city = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    iata = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airports'
    