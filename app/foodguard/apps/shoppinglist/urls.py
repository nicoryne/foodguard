# shopping_list/urls.py
from django.urls import path
from .views import (
    ShoppingListView,
    ShoppingListDetailView,
    ShoppingListIngredientCreateView,
    IngredientsToBuyListView,
    IngredientsInCartListView,
    IngredientInCartDeleteView,
)

urlpatterns = [
    path('', ShoppingListView.as_view(), name='shopping-list'),
    path('<int:pk>/', ShoppingListDetailView.as_view(), name='shopping-list-detail'),
    path('new/', ShoppingListIngredientCreateView.as_view(), name='shopping-list-ingredient-create'),
    path('<int:shopping_list_id>/ingredients/', IngredientsToBuyListView.as_view(), name='ingredients-to-buy-list'),
    path('<int:shopping_list_id>/cart/', IngredientsInCartListView.as_view(), name='ingredients-in-cart-list'),
    path('cart/<int:pk>/delete/', IngredientInCartDeleteView.as_view(), name='ingredient-in-cart-delete'),
]
