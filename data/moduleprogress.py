"""This file is used to manage the ModuleProgress entity in the database.
It contains the functions for creating, querying, editing and deleting a module progress from the database."""

import sqlite3
from pathlib import Path

# ------- CREATE NEW MODULEPROGRESS ---------------------------------------------------------------------------------------
def create_moduleprogress_entries(student_id: str, course_id: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM course_modules WHERE course_id = ?", (course_id,))
    moduleliste = cursor.fetchall()
    for module in moduleliste:
        module_id = module[1]
        cursor.execute("INSERT INTO moduleprogress (student_id, module_id, module_status) VALUES (?,?,?)", (student_id, module_id, "offen"))
    connection.commit()
    connection.close()

# --- QUERY MODULEPROGRESS ---------------------------------------------------------------------------------------------------
def get_overview_data(student_id: str) -> list:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM moduleprogress WHERE student_id = ?", (student_id,))
    modules_db = cursor.fetchall()
    modulelist = []
    for m in modules_db:
        module_id = m[1]
        module_status = m[2]
        module_grade = m[3]
        cursor.execute("SELECT * FROM modules WHERE module_id = ?", (module_id,))
        module_info = cursor.fetchone()
        module_name = module_info[1]
        module_etc = module_info[2]
        module = (module_id, module_name, module_etc, module_status, module_grade)
        modulelist.append(module)
    connection.close()
    return modulelist

def get_grade_data(student_id: str) -> list:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM moduleprogress WHERE student_id = ? AND module_grade != ?", (student_id, "None"))
    modules_db = cursor.fetchall()
    connection.close()
    return modules_db


# --- DB: SAVE MODULEPROGRESS-CHANGES WHILE SESSION  -----------------------------------------------------------------------------------
def save_modules_changes(student_id: str, module_id: str, module_status: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("UPDATE moduleprogress SET module_status = ? WHERE student_id = ? AND module_id = ?", (module_status, student_id, module_id))
    connection.commit()
    connection.close()
    print(f"Status wurde aktualisiert: {module_id}: {module_status}")

def save_grade_changes(student_id: str, module_id: str, module_grade: float):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("UPDATE moduleprogress SET module_grade = ? WHERE student_id = ? AND module_id = ?", (module_grade, student_id, module_id))
    connection.commit()
    connection.close()
    print(f"Note wurde aktualisiert: {module_id}: {module_grade}")