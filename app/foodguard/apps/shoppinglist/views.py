from .models import ShoppingList, IngredientInCart, IngredientToBuy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Shopping List View
class ShoppingListView(ListView):
    model = ShoppingList
    template_name = 'shopping_list.html'
    context_object_name = 'shopping_lists'

# Shopping List Detail View
class ShoppingListDetailView(DetailView):
    model = ShoppingList
    template_name = 'shopping_list_detail.html'
    context_object_name = 'shopping_list'

# Add Ingredient to Shopping List
class ShoppingListIngredientCreateView(CreateView):
    model = IngredientToBuy
    fields = ['ingredient', 'shopping_list', 'quantity']
    template_name = 'shopping_list_ingredient_form.html'
    success_url = '/shopping-lists/'

# List Ingredients in the Shopping List
class IngredientsToBuyListView(ListView):
    model = IngredientToBuy
    template_name = 'ingredients_to_buy_list.html'
    context_object_name = 'ingredients_to_buy'

    def get_queryset(self):
        # Filter ingredients by shopping list
        shopping_list_id = self.kwargs['shopping_list_id']
        return IngredientToBuy.objects.filter(shopping_list_id=shopping_list_id)

# Manage Ingredients in Cart
class IngredientsInCartListView(ListView):
    model = IngredientInCart
    template_name = 'ingredients_in_cart_list.html'
    context_object_name = 'ingredients_in_cart'

    def get_queryset(self):
        # Filter ingredients by shopping list
        shopping_list_id = self.kwargs['shopping_list_id']
        return IngredientInCart.objects.filter(shopping_list_id=shopping_list_id)

# Remove Ingredient from Cart
class IngredientInCartDeleteView(DeleteView):
    model = IngredientInCart
    template_name = 'ingredient_in_cart_confirm_delete.html'
    success_url = '/shopping-lists/'

