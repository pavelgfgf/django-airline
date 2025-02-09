from .models import Flight
from .serializer import FlightSerializer
from airport.models import Airport
from airport.serializer import AirportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class FlightList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        fromi = request.GET.get('fromi') 
        to = request.GET.get('to') 
        # date1 = request.GET.get('date1') 
        # date2 = request.GET.get('date2')
        # passengers = request.GET.get('passenger') 

        # Если есть query параметры print в консоль, если нет тогда выполнить код ниже
        if fromi and to:
            flights = Flight.objects.filter(
                Q(fromi__iata=fromi) & Q(to__iata=to)
            )
            serializer = FlightSerializer(flights, many=True)
            return Response({'items': serializer.data}, status=status.HTTP_200_OK)
        else: 
            flights = Flight.objects.all()
            serializer = FlightSerializer(flights, many=True)
            return Response({"items": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FlightDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Flight.objects.get(pk=pk)
        except Flight.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get(self, request, pk):
        flight = self.get_object(pk)
        serializer = FlightSerializer(flight)
        return Response(serializer.data)
    
    def put(self, request, pk):
        flight = self.get_object(pk)
        serializer = FlightSerializer(flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        flight = self.get_object(pk)
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

