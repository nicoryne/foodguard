from django.contrib import admin
from .models import ShoppingList, IngredientToBuy, IngredientInCart

@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('shopping_list_id', 'user', 'capacity')
    search_fields = ('user__fname', 'user__lname')

@admin.register(IngredientToBuy)
class IngredientToBuyAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'shopping_list', 'quantity', 'in_cart')
    list_filter = ('in_cart',)

@admin.register(IngredientInCart)
class IngredientInCartAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'shopping_list', 'quantity')
