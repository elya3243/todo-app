from django.urls import path
from .views import UserCreateAPIView, UserInfoView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('login/', obtain_auth_token, name='login'),
    path('userinfo/', UserInfoView.as_view(), name='userinfo')
]