from django.views import View
from .models import Recipe, RecipeIngredient, RecipeUserSaved, RecipeUserRating
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

# Recipe List View
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['trending_recipes'] = Recipe.objects.order_by('-rating')[:5]
        context['favorited_recipes'] = Recipe.objects.filter(
            recipe_user_saved__user=user, recipe_user_saved__is_favorite=True
        )
        return context

# Admin Recipe List
class AdminRecipeListView(ListView):
    model = Recipe
    template_name = 'admin_recipe_list.html'
    context_object_name = 'recipes'
    ordering = ['-created_at']  # Optional: Orders recipes by most recent

    def get_queryset(self):
        return Recipe.objects.all()

# Recipe Detail View
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        saved = RecipeUserSaved.objects.filter(user=user, recipe=self.object).first()
        context['is_favorite'] = saved.is_favorite if saved else False
        return context


# Favorite Recipe
class ToggleFavoriteView(View):
    def post(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        user = request.user
        saved, created = RecipeUserSaved.objects.get_or_create(user=user, recipe=recipe)
        saved.is_favorite = not saved.is_favorite
        saved.save()
        return redirect('recipe-detail', pk=recipe.pk)

# Create New Recipe
class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'description', 'difficulty', 'duration', 'rating', 'instructions']
    template_name = 'recipe_create_form.html'
    success_url = '/recipes/'

# Recipe Update View
class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'description', 'difficulty', 'duration', 'rating', 'instructions']
    template_name = 'recipe_update_form.html'
    success_url = '/recipes/'

# Recipe Delete View
class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipe_confirm_delete.html'
    success_url = '/recipes/'

# Recipe User Saved List View
class RecipeUserSavedListView(ListView):
    model = RecipeUserSaved
    template_name = 'recipe_user_saved_list.html'
    context_object_name = 'recipes_users_saved'

# Recipe User Saved Create View
class RecipeUserSavedCreate(CreateView):
    model = RecipeUserSaved
    fields = ['user', 'recipe', 'is_favorite']
    template_name ='recipe_user_saved_create_form.html'
    success_url = '/recipes/'

# Recipe User Rating List View
class RecipeUserRatingListView(ListView):
    model = RecipeUserRating
    template_name = 'recipe_user_rating_list.html'
    context_object_name = 'recipes_users_rated'

# Recipe User Rating Create View
class RecipeUserRatingCreate(CreateView):
    model = RecipeUserRating
    fields = ['user', 'recipe', 'rating']
    template_name = 'recipe_user_rating_create_form.html'
    success_url = '/recipes/'

# Recipe Ingredients List View
class RecipeIngredientListView(ListView):
    model = RecipeIngredient
    template_name = 'recipe_ingredient_list.html'
    context_object_name = 'ingredients'

    def get_queryset(self):
        # Get the recipe ID from the URL and filter ingredients
        recipe_id = self.kwargs['recipe_id']
        return RecipeIngredient.objects.filter(recipe_id=recipe_id)

# Recipe Ingredient Create View
class RecipeIngredientCreate(CreateView):
    model = RecipeIngredient
    fields = ['recipe', 'ingredient', 'quantity']
    template_name = 'recipe_ingredient_create_form.html'
    success_url = '/recipes/'
