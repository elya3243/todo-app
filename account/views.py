from rest_framework import generics
from .serializers import UserSerializer, UserInfoSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    model = User
    serializer_class = UserSerializer


class UserInfoView(generics.RetrieveAPIView):
    model = User
    serializer_class = UserInfoSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user
