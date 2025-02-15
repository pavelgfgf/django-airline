from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from booking.models import Booking
from booking.serializer import CreateBookingModelSerializer, RetrieveBookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateBookingModelSerializer
        elif self.action == "retrieve":
            return RetrieveBookingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={"data": serializer.data}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        booking_code = kwargs.get('pk')
        booking = get_object_or_404(Booking, code=booking_code)
        serializer = self.get_serializer(booking)
        return Response(data={"data": serializer.data}, status=status.HTTP_200_OK)
