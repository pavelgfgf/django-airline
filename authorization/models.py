from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=100)
    document_number = models.CharField(max_length=100)

    def __str__(self):
        return self.username