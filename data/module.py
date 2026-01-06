import sqlite3
from pathlib import Path

def new_modul_db(module_id: str, module_name: str, module_etc: int):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO modules (module_id, module_name, module_etc) VALUES (?,?,?)", (module_id, module_name, module_etc))
    connection.commit()
    connection.close()
    print("Modul wurde angelegt.")
