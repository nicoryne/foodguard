from django.db import models
from django.contrib.auth.models import User

# Classes within notifications/models.py
#   1. Notification


# Notification
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
        