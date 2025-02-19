from rest_framework import serializers
from .models import CustomUser


class RegistartionSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)
    first_name = serializers.CharField(max_length=128)
    last_name = serializers.CharField(max_length=128)
    document_number = serializers.CharField(max_length=128)

    def create(self, validated_data):
        password = validated_data["password"]
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'phone' , 'document_number']
