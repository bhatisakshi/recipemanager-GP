from rest_framework import serializers
from .models import Recipe, Ingredient, Category, RecipeIngredient, RecipeCategory

class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Recipe model.
    """

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'preparation_time', 'instructions']
    
    def validate_preparation_time(self, value):
        """
        Check that the preparation time is a positive number.
        """
        if value < 0:
            raise serializers.ValidationError("Preparation time must be a positive number.")
        return value

    def validate(self, data):
        """
        Object-level validation for Recipe.
        """
        if not data['title']:
            raise serializers.ValidationError("Title is required.")
        return data


class IngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Ingredient model.
    """

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity']

    def validate_quantity(self, value):
        """
        Check that the quantity is greater than zero.
        """
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        return value

    def validate(self, data):
        """
        Object-level validation for Ingredient.
        """
        if not data['name']:
            raise serializers.ValidationError("Ingredient name is required.")
        return data


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """

    class Meta:
        model = Category
        fields = ['id', 'name']

    def validate_name(self, value):
        """
        Check that the category name is not empty.
        """
        if not value.strip():
            raise serializers.ValidationError("Category name cannot be empty.")
        return value


class RecipeIngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for the RecipeIngredient model.
    """

    class Meta:
        model = RecipeIngredient
        fields = ['id', 'recipe', 'ingredient', 'quantity']

    def validate_quantity(self, value):
        """
        Check that the quantity is greater than zero.
        """
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        return value

    def validate(self, data):
        """
        Object-level validation for RecipeIngredient.
        """
        if data['recipe'] == data['ingredient']:
            raise serializers.ValidationError("Recipe and Ingredient cannot be the same.")
        return data


class RecipeCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the RecipeCategory model.
    """

    class Meta:
        model = RecipeCategory
        fields = ['id', 'recipe', 'category']

    def validate(self, data):
        """
        Object-level validation for RecipeCategory.
        """
        if data['recipe'] == data['category']:
            raise serializers.ValidationError("Recipe and Category cannot be the same.")
        return data
