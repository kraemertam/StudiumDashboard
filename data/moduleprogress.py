"""This file is used to manage the ModuleProgress entity in the database.
It contains the functions for creating, querying, editing and deleting a module progress from the database."""

import sqlite3
from pathlib import Path

# ------- CREATE NEW MODULEPROGRESS ---------------------------------------------------------------------------------------
def create_moduleprogress_entries_db(moduleprogress_rows: list[tuple]):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.executemany("INSERT INTO moduleprogress (student_id, module_id, module_status) VALUES (?,?,?)", moduleprogress_rows)
        connection.commit()
    finally:
        connection.close()


# --- QUERY MODULEPROGRESS ---------------------------------------------------------------------------------------------------
def get_moduleprogress_data_db(student_id: str) -> list:
    """All modules from student including status and grade.
    Returns in tuple per module, sorted by module_id: 
    (module_id, module_name, module_ects, module_status, module_grade)
    module_grade is None as long as no grade has been set."""
    
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    try: 
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("""
                SELECT m.module_id, m.module_name, m.module_ects, mp.module_status, mp.module_grade 
                FROM moduleprogress mp
                JOIN modules m ON m.module_id = mp.module_id
                WHERE mp.student_id = ?
                ORDER BY m.module_id""", (student_id,))
        return cursor.fetchall()
    finally:
        connection.close()

def get_grade_data_db(student_id: str) -> list:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM moduleprogress WHERE student_id = ? AND module_grade != ?", (student_id, "None"))
    modules_db = cursor.fetchall()
    connection.close()
    return modules_db


# --- DB: SAVE MODULEPROGRESS-CHANGES WHILE SESSION  -----------------------------------------------------------------------------------
def save_modulestatus_changes_db(student_id: str, module_id: str, module_status: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("UPDATE moduleprogress SET module_status = ? WHERE student_id = ? AND module_id = ?", (module_status, student_id, module_id))
    connection.commit()
    connection.close()
    print(f"Status wurde aktualisiert: {module_id}: {module_status}")

def save_grade_changes_db(student_id: str, module_id: str, module_grade: float):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("UPDATE moduleprogress SET module_grade = ? WHERE student_id = ? AND module_id = ?", (module_grade, student_id, module_id))
    connection.commit()
    connection.close()
    print(f"Note wurde aktualisiert: {module_id}: {module_grade}")