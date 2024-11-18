from .models import ShoppingList, IngredientInCart, IngredientToBuy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import ShoppingList, IngredientToBuy
from .forms import IngredientToBuyForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients_to_buy'] = IngredientToBuy.objects.filter(shopping_list=self.object)
        return context

# Add Ingredient to Shopping List
class ShoppingListIngredientCreateView(CreateView):
    model = IngredientToBuy
    form_class = IngredientToBuyForm
    template_name = 'shopping_list_ingredient_form.html'

    def get_success_url(self):
        return reverse_lazy('shopping-list-detail', kwargs={'pk': self.kwargs['shopping_list_id']})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        shopping_list = get_object_or_404(ShoppingList, pk=self.kwargs['shopping_list_id'])
        kwargs['initial'] = {'shopping_list': shopping_list}
        return kwargs

    def form_valid(self, form):
        form.instance.shopping_list = get_object_or_404(ShoppingList, pk=self.kwargs['shopping_list_id'])
        return super().form_valid(form)

class IngredientUpdateView(UpdateView):
    model = IngredientToBuy
    form_class = IngredientToBuyForm
    template_name = 'ingredient-update-form.html'

    def get_object(self, queryset=None):
        shopping_list_id = self.kwargs['shopping_list_id']  # Get the shopping list ID from the URL
        pk = self.kwargs['pk']  # Get the ingredient ID from the URL
        # Retrieve the object or return a 404
        return get_object_or_404(IngredientToBuy, pk=pk, shopping_list_id=shopping_list_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the shopping list to pass to the template
        shopping_list_id = self.kwargs['shopping_list_id']
        context['shopping_list'] = get_object_or_404(ShoppingList, pk=shopping_list_id)
        return context

    def get_success_url(self):
        return reverse_lazy('shopping-list-detail', kwargs={'pk': self.object.shopping_list.shopping_list_id})


class IngredientDeleteView(DeleteView):
    model = IngredientToBuy
    template_name = 'ingredient-confirm-delete.html'

    def get_success_url(self):
        return reverse_lazy('shopping-list-detail', kwargs={'pk': self.object.shopping_list.shopping_list_id})

    def get_object(self, queryset=None):
        shopping_list_id = self.kwargs['shopping_list_id']
        pk = self.kwargs['pk']
        return get_object_or_404(IngredientToBuy, pk=pk, shopping_list_id=shopping_list_id)


    
# List Ingredients in the Shopping List
class IngredientsToBuyListView(ListView):
    model = IngredientToBuy
    template_name = 'ingredients_to_buy_list.html'
    context_object_name = 'ingredients_to_buy'

    def get_queryset(self):
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

    def get_success_url(self):
        return reverse_lazy('shopping-list-detail', kwargs={'pk': self.object.shopping_list.shopping_list_id})


