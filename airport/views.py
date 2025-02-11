from .models import Airport
from .serializer import AirportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

class AirportList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        query = request.query_params.get('query', '')

        if query:
            airports = Airport.objects.filter(
                Q(airport__icontains=query) | Q(city__icontains=query) | Q(iata__iexact=query)
            )
        else:
            airports = Airport.objects.all()
        serializer = AirportSerializer(airports, many=True)
        return Response({'data': {'items': serializer.data}}, status=status.HTTP_200_OK)