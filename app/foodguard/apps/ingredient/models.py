from django.db import models

class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)  # Add this field for quantity
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ingredient/', null=True, blank=True)
    date_purchased = models.DateField(null=True, blank=True)  # Add this field for the purchase date
    expiry_date = models.DateField(null=True, blank=True)     # Add this field for expiry date

    def __str__(self):
        return f"Ingredient ID: {self.ingredient_id}\nName: {self.name}\nCategory: {self.category}"
    #ADD MORE IF YOU NEED TO VIEW MORE IN THE SHELL CONSOLE.