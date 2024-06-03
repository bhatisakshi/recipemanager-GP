# Recipe API

This is a RESTful API for managing recipes, ingredients, categories, and their associations. The API is built with Django and Django REST Framework.

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/recipe-api.git
   cd recipe-api
   ```
2. **Create a virtual environment and activate it:**
   ```sh
   virenv envname
   source venv/bin/activate
   ```
3. **Run the database migrations:**
   ```sh
   python manage.py migrate
   ```
4. **Start the development server:**
   ```sh
   python manage.py runserver
   ```
   

## Usage

Once the server is running, you can interact with the API using a tool like curl, Postman, or your web browser. <br><br>


## API Endpoints

### Recipe Endpoints
- GET /recipes/: Retrieve a list of all recipes.
- POST /recipes/: Create a new recipe.
- GET /recipes/{id}/: Retrieve a specific recipe by ID.
- UT /recipes/{id}/: Update a specific recipe by ID.
- DELETE /recipes/{id}/: Delete a specific recipe by ID.

### Ingredient Endpoints
- GET /ingredients/: Retrieve a list of all ingredients.
- POST /ingredients/: Create a new ingredient.
- GET /ingredients/{id}/: Retrieve a specific ingredient by ID.
- PUT /ingredients/{id}/: Update a specific ingredient by ID.
- DELETE /ingredients/{id}/: Delete a specific ingredient by ID.

### Category Endpoints
- GET /categories/: Retrieve a list of all categories.
- POST /categories/: Create a new category.
- GET /categories/{id}/: Retrieve a specific category by ID.
- PUT /categories/{id}/: Update a specific category by ID.
- DELETE /categories/{id}/: Delete a specific category by ID.

### RecipeIngredient Endpoints
- GET /recipe-ingredients/: Retrieve a list of all recipe ingredients.
- POST /recipe-ingredients/: Create a new recipe ingredient.
- GET /recipe-ingredients/{id}/: Retrieve a specific recipe ingredient by ID.
- PUT /recipe-ingredients/{id}/: Update a specific recipe ingredient by ID.
- DELETE /recipe-ingredients/{id}/: Delete a specific recipe ingredient by ID.
   
### RecipeCategory Endpoints
- GET /recipe-categories/: Retrieve a list of all recipe categories.
- POST /recipe-categories/: Create a new recipe category.
- GET /recipe-categories/{id}/: Retrieve a specific recipe category by ID.
- PUT /recipe-categories/{id}/: Update a specific recipe category by ID.
- DELETE /recipe-categories/{id}/: Delete a specific recipe category by ID.


## Models

### Recipe
- id: AutoField (Primary Key)
- title: CharField
- description: TextField
- preparation_time: IntegerField
- instructions: TextField

### Ingredient
- id: AutoField (Primary Key)
- name: CharField
- quantity: FloatField

### Category
- id: AutoField (Primary Key)
- name: CharField

### RecipeIngredient
- id: AutoField (Primary Key)
- recipe: ForeignKey (Recipe)
- ingredient: ForeignKey (Ingredient)
- quantity: FloatField

### RecipeCategory
- id: AutoField (Primary Key)
- recipe: ForeignKey (Recipe)
- category: ForeignKey (Category)


## Validation

### RecipeSerializer
- validate_preparation_time: Ensures the preparation time is a positive number.
- validate: Ensures the title is not empty.

### IngredientSerializer
- validate_quantity: Ensures the quantity is greater than zero.
- validate: Ensures the name is not empty.

### CategorySerializer
- validate_name: Ensures the category name is not empty.

### RecipeIngredientSerializer
- validate_quantity: Ensures the quantity is greater than zero.
- validate: Ensures that the recipe and ingredient are not the same.

### RecipeCategorySerializer
- validate: Ensures that the recipe and category are not the same.
