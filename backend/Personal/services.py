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

#Show personal detail 
def show_personal_detail():
    user_id = request.args.get('user_id')
    conn = get_db_connection()
    person = conn.execute(
    '''SELECT fullname,
            user_id,
            username,
            gender,
            weight,
            height,
            dob,
            avatar,
            activity_level  
    FROM users WHERE user_id = ?''',(user_id,)).fetchone ()
    conn.close()
    
    if person:
         return jsonify({
            'status': 'success',
            'data': {
                'user_id': person['user_id'],
                'avatar': person['avatar'],
                'fullname': person['fullname'],
                'username': person['username'],
                'gender': person['gender'],
                'dob': person['dob'],
                'height': person['height'],
                'weight': person['weight'],
                'activity_level': person['activity_level']
            }
        }), 200, {'Content-Type': 'application/json'}
    else:
        return jsonify({'status': 'error', 'message': 'Unavailable user'}), 404
    
#Update personal detail
def update_personal_detail():
        user_id = request.args.get('user_id')
        data = request.json 
        height = data.get('height')
        weight = data.get('weight')
        activity_level = data.get('activity_level')
        conn = get_db_connection()
        person = conn.execute("SELECT user_id FROM eating_histories WHERE user_id = ?", (user_id,)).fetchone()
        conn.close()
        
        if person:
            conn = get_db_connection()
            conn.execute("""
            UPDATE users SET height = ?, weight = ?, activity_level = ?
            WHERE user_id = ?
            """, (height,weight,activity_level,user_id,))
            conn.commit()
            conn.close()
            return jsonify({'status': 'success', 'message': 'Updated personal detail scuccessfully'}), 200 
        
        else:
            return jsonify({'status': 'error', 'message': 'Failed to update personal detail'}), 404
        
#Show nutrition history within 3 days
def show_history():
    user_id = request.args.get('user_id')
    conn = get_db_connection()
    
    user = conn.execute('SELECT user_id FROM eating_histories WHERE user_id = ?', (user_id,)).fetchone()
    conn.close()
    
    if user:
        conn = get_db_connection()
        nutrition_data = conn.execute(
            '''
            SELECT
                day,
                meal, 
                GROUP_CONCAT(recipes.name, ',') AS recipes,
                SUM(carbs) AS "total carbs",
                SUM(protein) AS "total protein",
                SUM(fat) AS "total fat",
                SUM(calories) AS "total calories"
            FROM eating_histories 
            JOIN recipes 
            ON eating_histories.recipe_id = recipes.recipe_id
            WHERE user_id = ? AND day >= date('now', '-3 days') AND eaten = 1
            GROUP BY day, meal
            ''', (user_id,)
        ).fetchall()  
        conn.close()
        
        result = [{
            'day': row['day'],
            'meal': row['meal'],
            'recipes': row['recipes'],
            'total carbs': row['total carbs'],
            'total protein': row['total protein'], 
            'total fat': row['total fat'],
            'total calories': row['total calories']
        } for row in nutrition_data]
        
        return jsonify({'status': 'success', 'data': result}), 200, {'Content-Type': 'application/json'}
    
    else:
        return jsonify({'status': 'error', 'message': 'User has not made any menu yet'}), 404

             
#Show today's nutrition history 
def show_nutrition_today():
    user_id = request.args.get('user_id')
    conn = get_db_connection()
    
    user = conn.execute('SELECT user_id FROM eating_histories WHERE user_id = ?', (user_id,)).fetchone()
    conn.close()
    
    if user:
        conn = get_db_connection()
        nutrition_data = conn.execute(
            '''
            SELECT 
                meal, 
                SUM(carbs) AS "total carbs",
                SUM(protein) AS "total protein",
                SUM(fat) AS "total fat",
                SUM(calories) AS "total calories"
            FROM eating_histories 
            JOIN recipes 
            ON eating_histories.recipe_id = recipes.recipe_id
            WHERE user_id = ? AND day = date('now') AND eaten = 1
            GROUP BY meal
            ''', (user_id,)
        ).fetchall()  
        conn.close()
    
        result = [{
            'meal': row['meal'],
            'total carbs': row['total carbs'],
            'total protein': row['total protein'], 
            'total fat': row['total fat'],
            'total calories': row['total calories']
        } for row in nutrition_data]
        
        return jsonify({'status': 'success', 'data': result}), 200, {'Content-Type': 'application/json'}
    
    else:
        return jsonify({'status': 'error', 'message': 'User has not made any menu yet'}), 404
