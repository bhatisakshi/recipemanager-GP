from django.contrib import admin
from .models import Recipe, Ingredient, Category, RecipeIngredient, RecipeCategory

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeCategory)
