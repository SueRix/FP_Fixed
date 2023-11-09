from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import CustomUser
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')


class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email format")
        return value

    def validate_password(self, value):
        password = value
        confirm_password = self.initial_data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match!")

        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long!")

        return value

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'token')
