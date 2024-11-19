from django import forms
from .models import IngredientToBuy
from ..ingredient.models import Ingredient

class IngredientToBuyForm(forms.ModelForm):
    class Meta:
        model = IngredientToBuy
        fields = ['ingredient', 'quantity'] 

