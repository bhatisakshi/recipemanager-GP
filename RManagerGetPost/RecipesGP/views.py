from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Recipe, Ingredient, Category, RecipeIngredient, RecipeCategory
from .serializers import RecipeSerializer, IngredientSerializer, CategorySerializer, RecipeIngredientSerializer, RecipeCategorySerializer

class RecipeListCreateAPIView(APIView):
    """
    API view to retrieve list of recipes or create a new recipe.
    """

    def get(self, request):
        """
        Retrieve all recipes.
        """
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new recipe.
        """
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetailAPIView(APIView):
    """
    API view to retrieve, update, or delete a recipe instance.
    """

    def get_object(self, pk):
        """
        Helper method to get the object with the given primary key (pk).
        """
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve a recipe by its pk.
        """
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a recipe by its pk.
        """
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a recipe by its pk.
        """
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IngredientListCreateAPIView(APIView):
    """
    API view to retrieve list of ingredients or create a new ingredient.
    """

    def get(self, request):
        """
        Retrieve all ingredients.
        """
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new ingredient.
        """
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientDetailAPIView(APIView):
    """
    API view to retrieve, update, or delete an ingredient instance.
    """

    def get_object(self, pk):
        """
        Helper method to get the object with the given primary key (pk).
        """
        try:
            return Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve an ingredient by its pk.
        """
        ingredient = self.get_object(pk)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update an ingredient by its pk.
        """
        ingredient = self.get_object(pk)
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete an ingredient by its pk.
        """
        ingredient = self.get_object(pk)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListCreateAPIView(APIView):
    """
    API view to retrieve list of categories or create a new category.
    """

    def get(self, request):
        """
        Retrieve all categories.
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new category.
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    """
    API view to retrieve, update, or delete a category instance.
    """

    def get_object(self, pk):
        """
        Helper method to get the object with the given primary key (pk).
        """
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve a category by its pk.
        """
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a category by its pk.
        """
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a category by its pk.
        """
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecipeIngredientListCreateAPIView(APIView):
    """
    API view to retrieve list of recipe ingredients or create a new recipe ingredient.
    """

    def get(self, request):
        """
        Retrieve all recipe ingredients.
        """
        recipeingredients = RecipeIngredient.objects.all()
        serializer = RecipeIngredientSerializer(recipeingredients, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new recipe ingredient.
        """
        serializer = RecipeIngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeIngredientDetailAPIView(APIView):
    """
    API view to retrieve, update, or delete a recipe ingredient instance.
    """

    def get_object(self, pk):
        """
        Helper method to get the object with the given primary key (pk).
        """
        try:
            return RecipeIngredient.objects.get(pk=pk)
        except RecipeIngredient.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve a recipe ingredient by its pk.
        """
        recipeingredient = self.get_object(pk)
        serializer = RecipeIngredientSerializer(recipeingredient)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a recipe ingredient by its pk.
        """
        recipeingredient = self.get_object(pk)
        serializer = RecipeIngredientSerializer(recipeingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a recipe ingredient by its pk.
        """
        recipeingredient = self.get_object(pk)
        recipeingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecipeCategoryListCreateAPIView(APIView):
    """
    API view to retrieve list of recipe categories or create a new recipe category.
    """

    def get(self, request):
        """
        Retrieve all recipe categories.
        """
        recipecategories = RecipeCategory.objects.all()
        serializer = RecipeCategorySerializer(recipecategories, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new recipe category.
        """
        serializer = RecipeCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeCategoryDetailAPIView(APIView):
    """
    API view to retrieve, update, or delete a recipe category instance.
    """

    def get_object(self, pk):
        """
        Helper method to get the object with the given primary key (pk).
        """
        try:
            return RecipeCategory.objects.get(pk=pk)
        except RecipeCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve a recipe category by its pk.
        """
        recipecategory = self.get_object(pk)
        serializer = RecipeCategorySerializer(recipecategory)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a recipe category by its pk.
        """
        recipecategory = self.get_object(pk)
        serializer = RecipeCategorySerializer(recipecategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a recipe category by its pk.
        """
        recipecategory = self.get_object(pk)
        recipecategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
