from .models import Flight
from .serializer import FlightSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class FlightList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        departure = request.GET.get('from') 
        arrival = request.GET.get('to') 
        date_1 = request.GET.get('date1')
        date_2 = request.GET.get('date2')
        passengers = request.GET.get('passenger') 

        flights_to = Flight.objects.filter(
                Q(from_field__iata=departure) & Q(to__iata=arrival)
            )
        serializer_to = FlightSerializer(flights_to, many=True, context={"date": date_1})

        flights_back = Flight.objects.filter(
                Q(from_field__iata=arrival) & Q(to__iata=departure)
            )
        serializer_back = FlightSerializer(flights_back if date_2 else [], many=True, context={"date": date_2, "passengers": passengers})
        return Response({"data": { "flight_to": serializer_to.data, "flights_back": serializer_back.data }})
