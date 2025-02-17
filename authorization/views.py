from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from .serializer import RegistartionSerializer, CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Registration(APIView):
    def post(self, request):
        serializer = RegistartionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        profile = CustomUser.objects.all()
        serializer = CustomUserSerializer(profile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    