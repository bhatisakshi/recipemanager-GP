from django.contrib import admin
from django.urls import path
from RecipesGP.views import(RecipeListCreateAPIView, 
                   RecipeDetailAPIView, 
                   IngredientListCreateAPIView, 
                   IngredientDetailAPIView,
                   CategoryListCreateAPIView,
                   CategoryDetailAPIView,
                   RecipeIngredientListCreateAPIView,
                   RecipeIngredientDetailAPIView,
                   RecipeCategoryListCreateAPIView,
                   RecipeCategoryDetailAPIView,
                   )

urlpatterns = [
    path('recipes/', RecipeListCreateAPIView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetailAPIView.as_view(), name='recipe-detail'),
    path('ingredients/', IngredientListCreateAPIView.as_view(), name='ingredient-list-create'),
    path('ingredients/<int:pk>/', IngredientDetailAPIView.as_view(), name='ingredient-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('recipeingredients/', RecipeIngredientListCreateAPIView.as_view(), name='recipeingredient-list-create'),
    path('recipeingredients/<int:pk>/', RecipeIngredientDetailAPIView.as_view(), name='recipeingredient-detail'),
    path('recipecategories/', RecipeCategoryListCreateAPIView.as_view(), name='recipecategory-list-create'),
    path('recipecategories/<int:pk>/', RecipeCategoryDetailAPIView.as_view(), name='recipecategory-detail'),
   
]
