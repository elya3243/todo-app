from rest_framework import serializers
from .models import Todo
from django.utils import timezone


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.due_date and instance.due_date < timezone.now():
            data['is_expire'] = True
        else:
            data['is_expire'] = False
        return data


class TodoStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['status']
