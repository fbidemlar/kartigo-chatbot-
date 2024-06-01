import sqlite3
import os


def add_product():
    try:
        database_path = 'diplom_database.db'
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        path = 'D:/diplom_kartigo/diplom_kartigo/backend/src/music/genres'
        contents = os.listdir(path)
        folders = [folder for folder in contents if os.path.isdir(os.path.join(path, folder))]

        for folder in folders:
            if conn:
                print(folder)
                cursor.execute('''
                    INSERT INTO genres (name)
                    VALUES (?)
                    ''', (folder,))

                conn.commit()
            else:
                conn.rollback()
        print("Готово!")
    except Exception as e:
        print(e)


add_product()

