from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeUserSaved

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_id', 'title', 'difficulty', 'duration', 'rating', 'created_at')
    search_fields = ('title', 'difficulty')
    list_filter = ('difficulty', 'created_at')
    ordering = ('-created_at',)

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity')
    search_fields = ('recipe__title', 'ingredient__name')

@admin.register(RecipeUserSaved)
class RecipeUserSavedAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'is_favorite')
    list_filter = ('is_favorite',)
