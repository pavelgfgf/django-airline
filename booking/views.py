from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Passenger, Booking
from .serializer import PassengerSerializer, PassengerCreateSerializer, BookingCreateSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BookingList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        passangers = Passenger.objects.all()
        serializer = PassengerSerializer(passangers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        passengers = request.data['passengers']
        flight = request.data['flight']

        booking_serializer = BookingCreateSerializer(data={'flight': flight})

        if booking_serializer.is_valid():
            booking = booking_serializer.save()
            booking_passengers = [{**passenger, 'booking': booking.id} for passenger in passengers]
            passenger_serializer = PassengerCreateSerializer(data=booking_passengers, many=True)

            if passenger_serializer.is_valid():
                passenger_serializer.save()
                return Response(passenger_serializer.data, status=status.HTTP_201_CREATED)
            return Response(passenger_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookingDetail(APIView):
    def get(self, request, pk):
        booking = Passenger.objects.get(pk=pk)
        serializer = PassengerSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)
