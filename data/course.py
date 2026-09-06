import sqlite3
from pathlib import Path


def new_course_db(course_id: str, course_name: str, course_title: str, course_etc: int):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO course (course_id, course_name, course_title, course_etc) VALUES (?,?,?,?)", (course_id, course_name, course_title, course_etc))
        connection.commit()
        print(f"Der Kurs {course_id}, {course_name} wurde in der Datenbank angelegt.")
    except sqlite3.IntegrityError:
        raise ValueError(f"Der Kurs {course_id}: {course_name} existiert in der Datenbank bereits.")
    finally:
        connection.close()

def check_course_db(course_id: str) -> bool:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * from course WHERE course_id = ?", (course_id))
    check = cursor.fetchone()
    connection.close()
    if check == None:
        return False
    else:
        return True

def get_course_db(course_id: str) -> tuple:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * from course WHERE course_id = ?", (course_id,))
    course = cursor.fetchone()
    print(course)
    cursor.execute("SELECT * from course_modules WHERE course_id = ?", (course_id,))
    moduleliste = cursor.fetchall()
    connection.commit()
    connection.close()
    print(course, moduleliste)
    return course, moduleliste

def get_all_courses_db() -> list:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * from course")
    list_of_courses = []
    for row in cursor.fetchall():
        list_of_courses.append(row)
    connection.commit()
    connection.close()
    return list_of_courses

def add_modules_to_course_db(course_id: str, module_id: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO course_modules (course_id, module_id) VALUES (?,?)", (course_id, module_id))
    connection.commit()
    connection.close()
    print(f"Das Modul {module_id} wurde dem Kurs {course_id} in der Datenbank hinzugefügt.")

get_course_db("FS-BAAKI-01")