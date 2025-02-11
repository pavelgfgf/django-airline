from rest_framework import serializers
from .models import CustomUser


class RegistartionSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):
        password = validated_data["password"]
        user = CustomUser.objects.create(username=validated_data["username"])
        user.set_password(password)
        user.save()
        return user 
    
class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=128)
    last_name = serializers.CharField(max_length=128)
    document_number = serializers.CharField(max_length=128)


