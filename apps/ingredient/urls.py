# ingredients/urls.py
from django.urls import path
from . import views 

app_name = "ingredient"

urlpatterns = [
    path('', views.ingredient_list_view, name='ingredient-list'),
    path('<int:pk>/', views.IngredientDetailView.as_view(), name='ingredient-detail'),
    path('new/', views.create_ingredient, name='ingredient-create'),
    path('<int:pk>/edit/', views.IngredientUpdateView.as_view(), name='ingredient-update'),
    path('<int:pk>/delete/', views.IngredientDeleteView.as_view(), name='ingredient-delete'),
]