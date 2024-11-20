from django.db import models
from ..users.models import User

# Classes within notifications/models.py
#   1. Notification


# Notification
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (
            f"Notification ID: {self.notification_id}\n"
            f"User: {self.user.fname} {self.user.lname}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Created At: {self.created_at}"
        )
        