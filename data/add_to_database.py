"""This file contains the functions for creating new students, courses, modules and connections in the database."""

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


def new_modul_db(module_id: str, module_name: str, module_etc: int):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO modules (module_id, module_name, module_etc) VALUES (?,?,?)", (module_id, module_name, module_etc))
    connection.commit()
    connection.close()
    print("Modul wurde angelegt.")


def new_course_db(course_id: str, course_name: str, course_title: str, course_etc: int):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO course (course_id, course_name, course_title, course_etc) VALUES (?,?,?,?)", (course_id, course_name, course_title, course_etc))
    connection.commit()
    connection.close()
    print("Course wurde angelegt.")

def add_modules_to_course(course_id: str, module_id: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO course_modules (course_id, module_id) VALUES (?,?)", (course_id, module_id))
    connection.commit()
    connection.close()
    print("Das Modul wurde dem Kurs hinzugefügt.")
