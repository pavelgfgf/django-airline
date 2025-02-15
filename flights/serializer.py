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
        print(self.context)
        cost = self.context.get('passengers', None) * instance.cost if self.context.get('passengers', None) is not None else instance.cost
        representation['cost'] = cost
        representation['from'] = {
            "city": instance.from_field.city,
            "airport": instance.from_field.name,
            "iata": instance.from_field.iata,
            "date": self.context['date'] if instance.time_from else None,
            "time": instance.time_from
        }
        representation['to'] = {
            "city": instance.to.city,
            "airport": instance.to.name,
            "iata": instance.to.iata,
            "date": self.context['date'] if instance.time_to else None,
            "time": instance.time_to
        }
        representation.pop('from_field', None)
        representation.pop('time_from', None)
        representation.pop('time_to', None)
        return representation

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        from_data = data.get('from', {})
        to_data = data.get('to', {})

        from_airport, _ = Airport.objects.get_or_create(
            iata=from_data.get('iata'),
            defaults={
                'city': from_data.get('city'),
                'name': from_data.get('airport')
            }
        )
        to_airport, _ = Airport.objects.get_or_create(
            iata=to_data.get('iata'),
            defaults={
                'city': to_data.get('city'),
                'name': to_data.get('airport')
            }
        )

        internal_value['from_field'] = from_airport
        internal_value['to'] = to_airport
        internal_value['time_from'] = from_data.get('time')
        internal_value['time_to'] = to_data.get('time')

        return internal_value
    