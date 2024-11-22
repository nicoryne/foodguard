from django.urls import path
from . import views

app_name = "shoppinglist"

urlpatterns = [
    path('', views.shopping_list_view, name='list_detail'),
    path('finish/', views.finish_list, name='finish_list'),
    path('add/', views.add_ingredient_to_buy, name='add_ingredient_to_buy'),
    path('toggle-in-cart/<int:ingredient_id>', views.toggle_to_cart, name='toggle_to_cart'),
    path('quantity-change/<int:ingredient_id>/<int:is_add>', views.quantity_change, name='quantity_change'),
    path('delete/', views.delete_ingredient_to_buy, name='delete_ingredient_to_buy')
]
