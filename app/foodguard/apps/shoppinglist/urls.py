from django.urls import path
from .views import ( shopping_list_view )

urlpatterns = [
    path('<int:list_id>/', shopping_list_view, name='shopping-list'),
   
]
