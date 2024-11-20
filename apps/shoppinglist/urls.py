from django.urls import path
from . import views

app_name = "shoppinglist"

urlpatterns = [
    path('<int:list_id>/', views.shopping_list_view, name='list_detail'),
    path('finish/<int:list_id>', views.finish_list, name='finish_list'),
    path('add/<int:list_id>', views.add_ingredient_to_buy, name='add_ingredient_to_buy')
]
