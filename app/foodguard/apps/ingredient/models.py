from django.db import models

# Classes within ingreient/models.py
#   1. Ingredient


# Ingredient
class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return f"Ingredient ID: {self.ingredient_id}\nName: {self.name}\nCategory: {self.category}"