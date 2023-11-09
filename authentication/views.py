from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import RegistrationSerializer, CustomUserSerializer
from rest_framework_jwt.settings import api_settings
from django.http import JsonResponse

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserRegistrationView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return JsonResponse({'message': 'Registration is successful!'})


class CustomLoginView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response({'token': token}, status=status.HTTP_200_OK)
