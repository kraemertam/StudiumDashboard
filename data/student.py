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

# --- GET OVERVIEW DATA -----------------------------------------------------------------------------------------------
def get_student_db(student_id: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * from student WHERE student_id = ?", (student_id,))
    student = cursor.fetchone()
    student_id = student[0]
    student_name = student[1]
    student_lastname = student[2]
    student_course = student[3]
    student_gradetarget = student[5]
    if student[3] == None:
        student_gradetarget = None
    else:
        cursor.execute("SELECT course_name, course_etc from course WHERE course_id = ?", (student[3],))
        course_info = cursor.fetchone()
        course_name = course_info[0]
        course_etc = course_info[1]
    connection.close()
    print(student_id, student_name, student_lastname, student_course, course_name, course_etc, student_gradetarget)
    return student_id, student_name, student_lastname, student_course, course_name, course_etc, student_gradetarget


def get_gradetarget(student_id: str) -> float:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT student_gradetarget FROM student WHERE student_id = ?", (student_id,))
    student_gradetarget = cursor.fetchone()
    connection.close()
    return student_gradetarget


# --- DB: ENROLL STUDENT IN COURSE ----------------------------------------------------------------------------------------
def enroll_course(student_id: str, course_id: str, student_gradetarget: float):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("UPDATE student SET student_course = ?, student_gradetarget=? WHERE student_id = ?", (course_id, student_semester, student_gradetarget, student_id))
    connection.commit()
    connection.close()
    print(f"{student_id} wurde in den Kurs {course_id} eingeschrieben.")
