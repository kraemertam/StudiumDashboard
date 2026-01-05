"""This file is used to manage the Student entity in the database.
It contains the functions for creating, editing and deleting a student from the database."""

import sqlite3
from pathlib import Path


def new_student_db(student_id: str, student_name: str, student_lastname: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO student (student_id, student_name, student_lastname) VALUES (?,?,?)", (student_id, student_name, student_lastname))
    connection.commit()
    connection.close()
    print("Student wurde angelegt.")

# --- DB: Save changes while session -----------------------------------------------------------------------------------
def save_modules_changes(student_id: str, module_id: str, module_status: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("UPDATE studentoverview SET module_status = ? WHERE student_id = ? AND module_id = ?", (module_status, student_id, module_id))
    connection.commit()
    connection.close()
    print(f"Status wurde aktualisiert: {module_id}: {module_status}")


def save_grade_changes(student_id: str, module_id: str, module_grade: float):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("UPDATE studentoverview SET module_grade = ? WHERE student_id = ? AND module_id = ?", (module_grade, student_id, module_id))
    connection.commit()
    connection.close()
    print(f"Status wurde aktualisiert: {module_id}: {module_grade}")
