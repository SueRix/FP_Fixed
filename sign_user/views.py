from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework_jwt.settings import api_settings
from django.http import JsonResponse

# from rest_framework.views import APIView

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserRegistrationView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return JsonResponse({**serializer.data, 'message': 'Registration is successful!'})


class CustomLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Please, input correct username and password.'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User with this name is not exists.'}, status=status.HTTP_400_BAD_REQUEST)

        if password == user.password:
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
