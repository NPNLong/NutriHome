from datetime import datetime
import sqlite3
# Connect to the SQLite database
DATABASE = 'nutrihome.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def fetch_calorie_chart(user_id):
    conn = get_db_connection()
    
    # Lấy chỉ tiêu calo của người dùng
    user = conn.execute("SELECT target_calories AS target_calories FROM users WHERE user_id = ?", (user_id,)).fetchone()
    if not user:
        conn.close()
        return {'status': 'error', 'message': 'User not found.'}, 404

    # Lấy ngày hiện tại dưới dạng chuỗi 'YYYY-MM-DD'
    today = datetime.now().strftime('%Y-%m-%d')

    # Tính toán tổng lượng calories hấp thụ từ các recipe của ngày hiện tại
    absorbedCalories = 0
    eating_history = conn.execute("""
        SELECT recipe_id 
        FROM eating_histories 
        WHERE user_id = ? AND day = ?
    """, (user_id, today)).fetchall()

    for entry in eating_history:
        recipe = conn.execute("""
            SELECT calories 
            FROM recipes 
            WHERE id = ?
        """, (entry['recipe_id'],)).fetchone()
        
        if recipe:
            absorbedCalories += recipe['calories']

    conn.close()

    # Trả về dữ liệu cho biểu đồ calo
    return {
        'status': 'success',
        'data': {
            'chart': {
                'goalCalories': user['target_calories'],
                'absorbedCalories': absorbedCalories
            }
        }
    }, 200
