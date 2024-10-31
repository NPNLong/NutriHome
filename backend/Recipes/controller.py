from flask import Blueprint
from .services import show_recipe
from .services import search_recipe_by_name
from .services import get_recipe_detail
from .services import add_recipe_to_menu

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

@recipes.route("/api/recipes/add-to-today-menu",methods =['POST'])
def add_to_menu():
    return add_recipe_to_menu()