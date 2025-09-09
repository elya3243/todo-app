from django.contrib.auth.models import User
from rest_framework import serializers
from todo.models import Todo


class UserSerializer(serializers.ModelSerializer):
    assigned_task_count = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'assigned_task_count']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

    def get_assigned_task_count(self, obj):
        return Todo.objects.filter(assigned_to=obj).count()


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'id', 'last_name', 'email', 'username']