from rest_framework import serializers
from .models import Booking, Passenger
from flights.serializer import FlightSerializer


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fiedls = ['flight']
        exclude = ['id']

class BookingSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)

    class Meta:
        model = Booking
        fiedls = '__all__'
        exclude = []

class PassengerCreateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Passenger
        fiedls = '__all__'
        exclude = []

class PassengerSerializer(serializers.ModelSerializer):
     booking = BookingSerializer(read_only=True)
     
     class Meta:
        model = Passenger
        fiedls = '__all__'
        exclude = []
