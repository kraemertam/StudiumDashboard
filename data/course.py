import sqlite3
from pathlib import Path

# CREATE NEW COURSE AND ADD MODULE TO COURSE
def new_course_db(course_id: str, course_name: str, course_title: str, course_ects: int):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO course (course_id, course_name, course_title, course_ects) VALUES (?,?,?,?)", (course_id, course_name, course_title, course_ects))
        connection.commit()
        print(f"Der Kurs {course_id}, {course_name} wurde in der Datenbank angelegt.")
    except sqlite3.IntegrityError:
        raise ValueError(f"Der Kurs {course_id}: {course_name} existiert in der Datenbank bereits.")
    finally:
        connection.close()

def add_modules_to_course_db(course_id: str, module_id: str):
    """Add a module to a course."""
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO course_modules (course_id, module_id) VALUES (?,?)", (course_id, module_id))
    connection.commit()
    connection.close()
    print(f"Das Modul {module_id} wurde dem Kurs {course_id} in der Datenbank hinzugefügt.")


# CHECKS AROUND COURSE
def check_course_db(course_id: str) -> bool:
    """Checks if course_id exists in DB."""
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * from course WHERE course_id = ?", (course_id, ))
    check = cursor.fetchone()
    connection.close()
    if check == None:
        return False
    else:
        return True

# GET DATA
def get_course_db(course_id) -> list:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    try: 
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("SELECT * from course WHERE course_id = ?", (course_id, ))
        return cursor.fetchone()
    finally:
        connection.close()

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

def get_modules_of_course_db(course_id: str) -> list[tuple]:
    """All modules of a course, sorted by position.
    Returns per module: (module_id, module_name, module_ects)"""
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.module_id, m.module_name, m.module_ects
            FROM course_modules cm
            JOIN modules m ON m.module_id = cm.module_id
            WHERE cm.course_id = ?
            ORDER BY cm.position""", (course_id,))
        return cursor.fetchall()
    finally:
        connection.close()