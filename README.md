# Recipe API

This is a RESTful API for managing recipes, ingredients, categories, and their associations. The API is built with Django and Django REST Framework.

## Table of Contents
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Validation](#validation)

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/recipe-api.git
   cd recipe-api
  ```
2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

Install the dependencies:
```sh
pip install -r requirements.txt
```

Run the database migrations:
```sh
python manage.py migrate
```

Start the development server:
```sh
python manage.py runserver
```
