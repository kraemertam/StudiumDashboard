"""This file is used to manage the Student entity in the database.
It contains the functions for creating, editing and deleting a student from the database. Also for query student-data."""

import sqlite3
from pathlib import Path

# --- CREATE NEW STUDENT ----------------------------------------------------------------------------------------------
def new_student_db(student_id: str, student_name: str, student_lastname: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO student (student_id, student_name, student_lastname) VALUES (?,?,?)", (student_id, student_name, student_lastname))
        connection.commit()
    except sqlite3.IntegrityError:
        raise ValueError(f"Die Matrikelnummer {student_id} existiert bereits unter dem Namen {student_name} {student_lastname}.")
    finally:
        connection.close()

# --- GET STUDENT DATA ----------------------------------------------------------------------------------------------
def get_student_db(student_id: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("SELECT * from student WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()
        connection.commit()
        return student
    finally:
        connection.close()

# --- CHECKS FOR STUDENT REGISTRATION ---------------------------------------------------------------------------------
def select_all_students_db()->list:
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

def check_student_db(student_id: str) -> bool:
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

def check_course_db(student_id: str) -> bool:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * from moduleprogress WHERE student_id = ?", (student_id,))
    check = cursor.fetchone()
    connection.close()
    if check == None:
        return False
    else:
        return True

def get_gradetarget_db(student_id: str) -> float:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT student_gradetarget FROM student WHERE student_id = ?", (student_id,))
    student_gradetarget = cursor.fetchone()
    connection.close()
    return student_gradetarget


# --- DB: ENROLL STUDENT IN COURSE ----------------------------------------------------------------------------------------
def enroll_student_in_course_db(student_id: str, course_id: str, student_gradetarget: float):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    try: 
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("SELECT 1 FROM course WHERE course_id = ?", (course_id,))
        course = cursor.fetchone()
        if course is None:
            raise ValueError(f"Der Kurs {course_id} existiert nicht.")
        cursor.execute("UPDATE student SET student_course = ?, student_gradetarget=? WHERE student_id = ?", (course_id, student_gradetarget, student_id))
        connection.commit()
    finally:
        connection.close()
