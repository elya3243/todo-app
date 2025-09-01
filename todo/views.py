from rest_framework import viewsets, status
from rest_framework.views import APIView
from django.db.models import Q
from .models import Todo, Status
from .serializers import TodoSerializer, TodoStatusSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    model = Todo
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Todo.objects.filter(
            Q(assigned_to=user) | Q(assigned_to__isnull=True)
        )
        status_param = self.request.query_params.get('status')
        if status_param:
            queryset = queryset.filter(status__name=status_param)

        return queryset


class TodoStatusUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({'error': 'todo not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TodoStatusSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
