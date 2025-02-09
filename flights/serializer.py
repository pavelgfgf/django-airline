from rest_framework import serializers
from .models import Flight, Airport


class AirportSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Airport
        fiealds = '__all__'
        exclude = []

class FlightSerializer(serializers.ModelSerializer):
    fromi = AirportSerializer(read_only=True)
    to = AirportSerializer(read_only=True)
    class Meta: 
        model = Flight
        fiealds = '__all__'
        exclude = []


    

