import random
import string
from datetime import date

from django.db import transaction
from rest_framework import serializers

from flights.models import Flight
from .models import Booking, Passenger


def generate_unique_code():
    return ''.join(random.choices(string.ascii_uppercase, k=5))


class CreatePassengerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ["first_name", "last_name", "birth_date", "document_number"]

    def validate(self, data):
        if not data:
            ValueError("Список пассажиров пуст")
        return data


class FlightModelSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    date = serializers.DateField()

    class Meta:
        model = Flight
        fields = ("id", "date")

    def validate_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Дата рейса не может быть в прошлом.")
        return value


class CreateBookingModelSerializer(serializers.ModelSerializer):
    passengers = CreatePassengerModelSerializer(many=True, write_only=True)
    flight_from = FlightModelSerializer(required=True, write_only=True)
    flight_back = FlightModelSerializer(required=False, write_only=True)

    class Meta:
        model = Booking
        fields = ("passengers", "flight_from", "flight_back", "code")
        read_only_fields = ("code", )

    def create(self, validated_data):
        passengers_data = validated_data.pop("passengers")
        flight_from_data = validated_data.pop("flight_from")
        flight_back_data = validated_data.pop("flight_back")

        if len(passengers_data) > 8:
            ValueError("Слишком много пассажиров в бронировании")

        flight_from_instance = Flight.objects.filter(id=flight_from_data["id"]).first()
        if not flight_from_instance:
            raise ValueError(f"Рейса с id {flight_from_data['id']} нет в базе")
        if flight_from_instance.get_availability_for_date(flight_from_data["date"]) < len(passengers_data):
            raise ValueError(f"В выбранном рейсе {flight_from_data} не свободных хватает мест")

        flight_back_instance = None
        if flight_back_data:
            flight_back_instance = Flight.objects.filter(id=flight_back_data["id"]).first()
            if not flight_back_instance:
                raise ValueError(f"Рейса с id {flight_back_data['id']} нет в базе")

            if flight_back_instance.get_availability_for_date(flight_back_data["date"]) < len(passengers_data):
                raise ValueError(f"В выбранном рейсе {flight_back_data} не свободных хватает мест")

        code = generate_unique_code()
        for i in range(5):
            if Booking.objects.filter(code=code):
                code = generate_unique_code()
            else:
                break
        else:
            raise Exception("Error")

        with transaction.atomic():
            booking = Booking.objects.create(
                flight_from=flight_from_instance,
                flight_back=flight_back_instance,
                date_from=flight_from_data["date"],
                date_back=flight_back_data["date"] if flight_back_data else None,
                code=code,
            )

            for passenger_data in passengers_data:
                Passenger.objects.create(booking=booking, **passenger_data)

        return booking


class RetrieveBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ("code",)
