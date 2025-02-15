from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from booking.models import Booking, Passenger
from booking.serializer import CreateBookingModelSerializer
from flights.models import Flight


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateBookingModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={"data": serializer.data}, status=status.HTTP_201_CREATED)
