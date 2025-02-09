from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    birth_date = models.DateField()
    document_number = models.CharField(max_length=75)

    def __str__(self):
        return self.first_name