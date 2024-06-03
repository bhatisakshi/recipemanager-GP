from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    preparation_time = models.IntegerField()  # in minutes
    instructions = models.TextField()

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.title}"

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recipe.title} is a {self.category.name}"
