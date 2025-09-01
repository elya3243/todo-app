from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, TodoStatusUpdateAPIView

router = DefaultRouter()

router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
    path('todos/<int:pk>/update-status/', TodoStatusUpdateAPIView.as_view()),
]
