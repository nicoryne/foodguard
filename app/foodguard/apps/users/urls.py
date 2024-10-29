# users/urls.py
from django.urls import path
from .views import (
    UserListView,
    UserDetailView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
)

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('new/', UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/edit/', UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
