import sqlite3
from pathlib import Path

def new_module_db(module_id: str, module_name: str, module_ects: int):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO modules (module_id, module_name, module_ects) VALUES (?,?,?)", (module_id, module_name, module_ects))
        connection.commit()
    except sqlite3.IntegrityError:
        raise ValueError(f"Das Modul mit der ID {module_id} existiert bereits unter dem Namen {module_name}.")
    finally:
        connection.close()

def get_module_db(module_id: str) -> list:
        db_path = Path(__file__).resolve().parent / "databank.db"
        connection = sqlite3.connect(db_path)
        try:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()
            cursor.execute("SELECT * from modules WHERE module_id = ?", (module_id,))
            module = cursor.fetchone()
            connection.commit()
            return module
        finally:
            connection.close()


def check_module_db(module_id: str) -> bool:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * from modules WHERE module_id = ?", (module_id,))
    check = cursor.fetchone()
    connection.close()
    if check == None:
        return False
    else:
        return True

def select_all_modules_db()->list:
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    connection.execute("PRAGMA foreign_keys = ON")
    cursor.execute("SELECT * from modules")
    list_of_modules = []
    for row in cursor.fetchall():
        list_of_modules.append(row)
    connection.commit()
    connection.close()
    return list_of_modules