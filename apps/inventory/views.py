from .models import Inventory, InventoryIngredientOwnership
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Inventory List View
class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory_list.html'
    context_object_name = 'inventories'

# Inventory Detail View
class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory_detail.html'
    context_object_name = 'inventory'

# Inventory Create View (Add Inventory)
class InventoryCreateView(CreateView):
    model = Inventory
    fields = ['ingredient_quantity', 'user']
    template_name = 'inventory_create_form.html'
    success_url = '/inventory/'

# Inventory Update View
class InventoryUpdateView(UpdateView):
    model = Inventory
    fields = ['ingredient_quantity']
    template_name = 'inventory_update_form.html'
    success_url = '/inventory/'

# Inventory Delete View
class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory_confirm_delete.html'
    success_url = '/inventory/'

# Add Ingredients to Inventory (Create View)
class InventoryIngredientCreateView(CreateView):
    model = InventoryIngredientOwnership
    fields = ['ingredient', 'inventory', 'purchase_date', 'expiry_date', 'quantity']
    template_name = 'inventory_ingredient_form.html'
    success_url = '/inventory/'

# Inventory Ingredient Ownership List View
class InventoryIngredientOwnershipListView(ListView):
    model = InventoryIngredientOwnership
    template_name = 'inventory_ingredient_list.html'
    context_object_name = 'ingredient_ownerships'

    def get_queryset(self):
        return InventoryIngredientOwnership.objects.filter(inventory=self.kwargs['pk'])

# Inventory Ingredient Ownership Detail View
class InventoryIngredientOwnershipDetailView(DetailView):
    model = InventoryIngredientOwnership
    template_name = 'inventory_ingredient_detail.html'
    context_object_name = 'ingredient_ownership'

# Inventory Ingredient Ownership Update View
class InventoryIngredientOwnershipUpdateView(UpdateView):
    model = InventoryIngredientOwnership
    fields = ['ingredient', 'purchase_date', 'expiry_date', 'quantity']
    template_name = 'inventory_ingredient_update_form.html'
    success_url = '/inventory/'

# Inventory Ingredient Ownership Delete View
class InventoryIngredientOwnershipDeleteView(DeleteView):
    model = InventoryIngredientOwnership
    template_name = 'inventory_ingredient_confirm_delete.html'
    success_url = '/inventory/'
