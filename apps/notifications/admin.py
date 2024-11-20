from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('notification_id', 'user', 'title', 'created_at')
    search_fields = ('user__fname', 'user__lname', 'title')
    list_filter = ('created_at',)
