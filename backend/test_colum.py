import sqlite3

def check_table_structure():
    conn = sqlite3.connect('nutrihome.db')  # Thay bằng đường dẫn tới tệp .db của bạn
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(eating_histories);")
    columns = cursor.fetchall()
    conn.close()

    # In thông tin về các cột
    for column in columns:
        print(column)

check_table_structure()

