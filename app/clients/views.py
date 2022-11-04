from rest_framework import generics
from .serializers import ClientDetailSerializer, ClientsListSerializer
from .models import Client
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import LoginSerializer
from .serializers import RegistrationSerializer

class ClientCreateView(generics.CreateAPIView):
    serializer_class = ClientDetailSerializer


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientsListSerializer
    queryset = Client.objects.all()


# class ClientLoginView(generics.CreateAPIView):
#     serializer_class = ClientLoginSerializer


class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)