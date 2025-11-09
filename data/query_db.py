import sqlite3
from pathlib import Path

# --- Datenbankabfragen ---

def select_student_db()->list:
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    connection.execute("PRAGMA foreign_keys = ON")
    cursor.execute("SELECT * from student")
    list_of_students = []
    for row in cursor.fetchall():
        list_of_students.append(row)
    connection.commit()
    connection.close()
    return list_of_students


def check_student(student_id: str) -> bool:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * from student WHERE student_id = ?", (student_id,))
    check = cursor.fetchone()
    connection.close()
    if check == None:
        return False
    else:
        return True

def get_student(student_id: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * from student WHERE student_id = ?", (student_id,))
    student = cursor.fetchone()
    connection.close()
    return student

def get_overview_data(student_id: str) -> list:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM studentoverview WHERE student_id = ?", (student_id,))
    modulliste = cursor.fetchall()

    connection.close()
    return modulliste
