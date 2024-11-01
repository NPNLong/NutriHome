from flask import Flask, request, jsonify
import sqlite3
import datetime
import json 
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

DATABASE = 'nutrihome.db'
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Show the list of recipe
def show_recipe():
        conn = get_db_connection()
        recipes = conn.execute("SELECT * FROM recipes").fetchall()
        conn.close()
        
        if recipes:
            recipe_dict = {
                    f"recipe_id = {recipe['recipe_id']}":{
                        'name': recipe['name'],
                        'image': recipe['image'],
                        'cooking_time': recipe['cooking_time'],
                        'rating': recipe['rating']
                    }
                for recipe in recipes
            }
            return jsonify({
                'status': 'success',
                'data': recipe_dict
            }), 200
        else:
            return jsonify({
                'status': 'error'
            }), 404

# Search recipe by name 
def search_recipe_by_name(name):
        conn = get_db_connection()
        recipe = conn.execute("SELECT * FROM recipes WHERE name = ?", (name,)).fetchone()
        conn.close()
        
        if recipe:
            return jsonify({
               f"recipe_id = {recipe['recipe_id']}":{
                        'name': recipe['name'],
                        'image': recipe['image'],
                        'cooking_time': recipe['cooking_time'],
                        'rating': recipe['rating']
                }
        }), 200

        else:
            return jsonify({
                'status': 'error',
                'message': 'No recipe found'
            }), 404
    
#Get the detail of a recipe
def get_recipe_detail():
    recipe_id = request.args.get('recipe_id')
    conn = get_db_connection()
    recipe = conn.execute("""
    SELECT name, 
        image, 
        cooking_time, 
        rating, 
        ingredients, 
        steps, 
        carbs, 
        protein, 
        fat, 
        calories
    FROM recipes WHERE recipe_id = ?
    """, (recipe_id,)).fetchone()
    conn.close()
    
    if recipe:
        return jsonify({
            'status': 'success',
            "data":{
                'name': recipe['name'],
                'image': recipe['image'],
                'cooking_time': recipe['cooking_time'],
                'rating': recipe['rating'],
                'ingredients': json.loads(recipe['ingredients']),
                'steps': json.loads(recipe['steps']),
                'nutrition_detail':{
                    'carbs': recipe['carbs'],
                    'protein': recipe['protein'],
                    'fat': recipe['fat'],
                    'calories': recipe['calories']
                }
            }
        }), 200, {'Content-Type': 'application/json'}
    else:
        return jsonify({'status': 'error', 'message': 'Unavailable recipe'}), 404
    
#Add a recipe to the today menu 
def add_recipe_to_menu():
    user_id = request.args.get('user_id')
    recipe_id = request.args.get('recipe_id')
    data = request.json 
    meal = data.get('meal')
    
    conn = get_db_connection()
    recipe = conn.execute("SELECT recipe_id FROM recipes WHERE recipe_id = ?", (recipe_id,)).fetchone()
    conn.close()
    
    if recipe:
        conn = get_db_connection()
        conn.execute("""
        INSERT INTO eating_histories (user_id,recipe_id, day,meal,eaten)
        VALUES (?, ?, date('now'), ?,1)
        """, (user_id,recipe_id, meal))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success', 'message': 'Recipe added to today menu'}), 200 
    
    else:
        return jsonify({'status': 'error', 'message': 'Unavailable recipe'}), 404
    
#Delete a recipe from today menu 
def delete_recipe_from_menu():
    eating_history_id = request.args.get('eating_history_id')
    conn = get_db_connection()

    eating_history = conn.execute("SELECT recipe_id FROM eating_histories WHERE eating_history_id = ?", (eating_history_id,)).fetchone()
    conn.close()
    
    if eating_history:
        conn = get_db_connection()
        conn.execute("DELETE FROM eating_histories WHERE eating_history_id = ?", (eating_history_id,))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success', 'message': 'Recipe deleted from today menu'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Unavailable history recorded'}), 404
        
    
    