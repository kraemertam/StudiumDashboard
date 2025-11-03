import os
import sqlite3

def studentcheck(name):
    name_check = name
    db_check = f"{name_check}.db"
    print(db_check)

    if os.path.exists(db_check):
        print("Datei ist vorhanden")
    else:
        connection = sqlite3.connect(db_check)
        cursor = connection.cursor()
        cursor.execute(f"""
        CREATE TABLE {name_check} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            vorname TEXT,
            geburtstag TEXT
        )
        """)

        connection.commit()
        connection.close()

studentcheck("jessica")
