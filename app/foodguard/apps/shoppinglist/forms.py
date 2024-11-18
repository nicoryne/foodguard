from django import forms
from .models import IngredientToBuy
from ..ingredient.models import Ingredient

class IngredientToBuyForm(forms.ModelForm):
    class Meta:
        model = IngredientToBuy
        fields = ['ingredient', 'quantity']  # Include ingredient and quantity fields
        widgets = {
            'shopping_list': forms.HiddenInput(),  # Hide the shopping list field since it's set in the view
        }

    def __init__(self, *args, **kwargs):
        # If there's an initial shopping_list provided, set it in the form
        self.shopping_list = kwargs.pop('initial', {}).get('shopping_list', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        # Set the shopping_list for the ingredient before saving
        ingredient_to_buy = super().save(commit=False)
        if self.shopping_list:
            ingredient_to_buy.shopping_list = self.shopping_list
        if commit:
            ingredient_to_buy.save()
        return ingredient_to_buy