# blog/urls.py
from django.urls import path
from .views import (
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
    RecipeUserSavedListView,
    RecipeUserSavedCreate,
    RecipeUserRatingListView,
    RecipeUserRatingCreate,
    RecipeIngredientListView,
    RecipeIngredientCreate
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('user/saved/', RecipeUserSavedListView.as_view(), name='recipe-user-saved-list'),
    path('user/saved/new/', RecipeUserSavedCreate.as_view(), name='recipe-user-saved-create'),
    path('user/ratings/', RecipeUserRatingListView.as_view(), name='recipe-user-rating-list'),
    path('user/ratings/new/', RecipeUserRatingCreate.as_view(), name='recipe-user-rating-create'),
    path('recipe/<int:recipe_id>/ingredients/', RecipeIngredientListView.as_view(), name='recipe-ingredient-list'),
    path('recipe/ingredients/new/', RecipeIngredientCreate.as_view(), name='recipe-ingredient-create'),
]
