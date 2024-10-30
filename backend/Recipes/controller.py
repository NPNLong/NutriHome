from flask import Blueprint
from .services import show_recipe
from .services import search_recipe_by_name
from .services import get_recipe_detail

recipes = Blueprint("recipes", __name__)

@recipes.route("/api/recipes", methods =['GET'])
def show_recipes():
    return show_recipe()

@recipes.route("/api/recipes/<name>", methods=['GET'])
def search_recipe(name):
    return search_recipe_by_name(name)

@recipes.route("/api/recipes/detail", methods=['GET'])
def get_detail():
    return get_recipe_detail()
    