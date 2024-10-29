from flask import Blueprint
from .services import get_recipe_by_name

recipes = Blueprint("recipes", __name__)

@recipes.route("/api/recipes/<name>", methods=['GET'])
def get_recipe(name):
    return get_recipe_by_name(name)
