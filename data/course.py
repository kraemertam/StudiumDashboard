import sqlite3
from pathlib import Path


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
