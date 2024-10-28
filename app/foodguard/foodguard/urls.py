"""
URL configuration for foodguard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView
from .views import (
    UserListView, UserDetailView, UserCreateView, 
    InventoryListView, InventoryDetailView, InventoryIngredientCreateView,
    RecipeListView, RecipeDetailView, RecipeCreateView, save_recipe, 
    ShoppingListView, ShoppingListIngredientCreateView
)

urlpatterns = [
    path('', TemplateView.as_view(template_name='landing_page.html'), name='landing_page'),

    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    
    path('inventory/', InventoryListView.as_view(), name='inventory_list'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail'),
    path('inventory/ingredient/add/', InventoryIngredientCreateView.as_view(), name='inventory_ingredient_add'),

    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/<int:recipe_id>/save/', save_recipe, name='save_recipe'),

    path('shopping-lists/', ShoppingListView.as_view(), name='shopping_list'),
    path('shopping-lists/create/', ShoppingListIngredientCreateView.as_view(), name='shopping_list_add'),
]

