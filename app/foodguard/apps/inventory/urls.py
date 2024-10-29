# inventory/urls.py
from django.urls import path
from .views import (
    InventoryListView,
    InventoryDetailView,
    InventoryCreateView,
    InventoryUpdateView,
    InventoryDeleteView,
    InventoryIngredientCreateView,
    InventoryIngredientOwnershipListView,
    InventoryIngredientOwnershipDetailView,
    InventoryIngredientOwnershipUpdateView,
    InventoryIngredientOwnershipDeleteView
)

urlpatterns = [
    path('', InventoryListView.as_view(), name='inventory-list'),
    path('new/', InventoryCreateView.as_view(), name='inventory-create'),
    path('<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),
    path('<int:pk>/edit/', InventoryUpdateView.as_view(), name='inventory-update'),
    path('<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory-delete'),
    
    path('<int:pk>/ingredients/', InventoryIngredientOwnershipListView.as_view(), name='ingredient-ownership-list'),
    path('ingredient/new/', InventoryIngredientCreateView.as_view(), name='ingredient-create'),
    path('ingredient/<int:pk>/', InventoryIngredientOwnershipDetailView.as_view(), name='ingredient-ownership-detail'),
    path('ingredient/<int:pk>/edit/', InventoryIngredientOwnershipUpdateView.as_view(), name='ingredient-ownership-update'),
    path('ingredient/<int:pk>/delete/', InventoryIngredientOwnershipDeleteView.as_view(), name='ingredient-ownership-delete'),
]
