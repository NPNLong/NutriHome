from flask import Flask, request, jsonify
import sqlite3
import datetime
import json 

DATABASE = 'nutrihome.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_recipe_by_name(name):
    try:
        conn = get_db_connection()
        recipe = conn.execute("SELECT * FROM recipes WHERE name = ?", (name,)).fetchone()
        conn.close()
        
        if recipe:
            return jsonify({
                'status': 'success',
                'data': {
                    'name': recipe['name'],
                    'image': recipe['image'],
                    'cooking_time': recipe['cooking_time'],
                    'rating': recipe['rating']
                }
            }), 200, {'Content-Type': 'application/json'}
        else:
            return jsonify({'status': 'error', 'message': 'Unavailable recipe'}), 404
    except Exception as e:
        print(f"Error occurred: {e}")  # Log lỗi vào console để kiểm tra chi tiết
        return jsonify({'status': 'error', 'message': 'Internal Server Error'}), 500
