from rest_framework import generics, viewsets, filters
from .serializers import UserSerializer, UserInfoSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAdminUser


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


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'first_name']
