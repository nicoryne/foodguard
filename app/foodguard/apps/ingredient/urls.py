# ingredients/urls.py
from django.urls import path
from .views import (
    IngredientListView,
    IngredientDetailView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView
)

urlpatterns = [
    path('', IngredientListView.as_view(), name='ingredient-list'),
    path('<int:pk>/', IngredientDetailView.as_view(), name='ingredient-detail'),
    path('new/', IngredientCreateView.as_view(), name='ingredient-create'),
    path('<int:pk>/edit/', IngredientUpdateView.as_view(), name='ingredient-update'),
    path('<int:pk>/delete/', IngredientDeleteView.as_view(), name='ingredient-delete'),
]
