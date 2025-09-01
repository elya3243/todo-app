from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['status']
