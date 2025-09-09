from django.urls import path
from .views import UserCreateAPIView, UserInfoView, UserViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
                  path('create/', UserCreateAPIView.as_view(), name='user_create'),
                  path('login/', obtain_auth_token, name='login'),
                  path('userinfo/', UserInfoView.as_view(), name='userinfo'),
              ] + router.urls
