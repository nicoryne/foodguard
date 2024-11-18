from django.shortcuts import render
from .models import ShoppingList

# Shopping List View
def shopping_list_view(request, list_id):
    shopping_list = ShoppingList.objects.prefetch_related('ingredients_to_buy').get(pk=list_id)
    ingredients = shopping_list.ingredients_to_buy.all()

    # Calculate total items, items in cart, and items left
    total_items = ingredients.count()
    items_in_cart = ingredients.filter(in_cart=True).count()
    items_left = total_items - items_in_cart

    context = {
        'shopping_list': shopping_list,
        'ingredients': ingredients,
        'total_items': total_items,
        'items_in_cart': items_in_cart,
        'items_left': items_left,
    }
    return render(request, 'shopping_list.html', context)




