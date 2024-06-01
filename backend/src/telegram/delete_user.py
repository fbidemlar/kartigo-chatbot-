import sqlite3

def delete_user():
    try:
        database_path = 'diplom_database.db'
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        if conn:
            cursor.execute('''DELETE FROM products''')
            conn.commit()
        else:
            conn.rollback()
        print("deleted!!")
    except Exception as e:
        print("ERRORRRR:", e)


delete_user()