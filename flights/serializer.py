from rest_framework import serializers
from .models import Flight, Airport

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['city', 'name', 'iata']

class FlightSerializer(serializers.ModelSerializer):
    from_field = AirportSerializer(read_only=True)
    to = AirportSerializer(read_only=True)

    class Meta:
        model = Flight
        fields = [
            'id', 'flight_code', 'from_field', 'to', 
            'time_from', 'time_to', 'cost'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        flightInstance = Flight.objects.get(pk=representation["id"])
        date = self.context.get('date', None)
        cost = self.context.get('passengers', None) * instance.cost if self.context.get('passengers', None) is not None else instance.cost
        representation['cost'] = cost
        representation['from'] = {
            "city": instance.from_field.city,
            "airport": instance.from_field.name,
            "iata": instance.from_field.iata,
            "date": date,
            "time": instance.time_from
        }
        representation['to'] = {
            "city": instance.to.city,
            "airport": instance.to.name,
            "iata": instance.to.iata,
            "date": date,
            "time": instance.time_to
        }
        representation["availability"] = flightInstance.get_availability_for_date(date)
        representation.pop('from_field', None)
        representation.pop('time_from', None)
        representation.pop('time_to', None)
        return representation
    