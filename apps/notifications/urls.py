# notifications/urls.py
from django.urls import path
from .views import (
    NotificationListView,
    NotificationDetailView,
    NotificationCreateView,
    NotificationUpdateView,
    NotificationDeleteView
)

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('new/', NotificationCreateView.as_view(), name='notification-create'),
    path('<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),
    path('<int:pk>/edit/', NotificationUpdateView.as_view(), name='notification-update'),
    path('<int:pk>/delete/', NotificationDeleteView.as_view(), name='notification-delete'),
]
