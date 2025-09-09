from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=88)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='todos')
    create_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos', null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
