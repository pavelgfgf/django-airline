from rest_framework import serializers
from .models import Booking
from flights.serializer import FlightSerializer


class BookingSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    class Meta:
        model = Booking
        fieadls = ['flight','first_name', 'last_name', 'document_number']
        exclude = ['id']

