"""This file is used to manage the Student entity in the database.
It contains the functions for creating, editing and deleting a student from the database. Also for query student-data."""

import sqlite3
from pathlib import Path

# --- CREATE NEW STUDENT ----------------------------------------------------------------------------------------------
def new_student_db(student_id: str, student_name: str, student_lastname: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO student (student_id, student_name, student_lastname) VALUES (?,?,?)", (student_id, student_name, student_lastname))
    connection.commit()
    connection.close()
    print("Student wurde angelegt.")

# --- CHECKS FOR STUDENT REGISTRATION ---------------------------------------------------------------------------------
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


def check_course(student_id: str) -> bool:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * from studentoverview WHERE student_id = ?", (student_id,))
    check = cursor.fetchone()
    connection.close()
    if check == None:
        return False
    else:
        return True

# --- GET OVERVIEW DATA -----------------------------------------------------------------------------------------------
def get_student(student_id: str):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * from student WHERE student_id = ?", (student_id,))
    student = cursor.fetchone()
    print(student)
    student_id = student[0]
    student_name = student[1]
    student_lastname = student[2]
    student_course = student[3]
    student_semester = student[4]
    student_gradetarget = student[5]
    if student[3] == None:
        course_name = None
        course_etc = None
        student_gradetarget = None
    else:
        cursor.execute("SELECT course_name, course_etc from course WHERE course_id = ?", (student[3],))
        course_info = cursor.fetchone()
        course_name = course_info[0]
        course_etc = course_info[1]
    connection.close()
    print(student_id, student_name, student_lastname, student_course, course_name, course_etc, student_semester, student_gradetarget)
    return student_id, student_name, student_lastname, student_course, course_name, course_etc, student_semester, student_gradetarget


def get_overview_data(student_id: str) -> list:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM studentoverview WHERE student_id = ?", (student_id,))
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
    cursor.execute("SELECT * FROM studentoverview WHERE student_id = ? AND module_grade != ?", (student_id, "None"))
    modules_db = cursor.fetchall()
    connection.close()
    return modules_db

def get_gradetarget(student_id: str) -> float:
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT student_gradetarget FROM student WHERE student_id = ?", (student_id,))
    student_gradetarget = cursor.fetchone()
    connection.close()
    return student_gradetarget


# --- ENROLL STUDENT IN COURSE ----------------------------------------------------------------------------------------
def enroll_course(student_id: str, course_id: str, student_semester: int, student_gradetarget: float):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM course_modules WHERE course_id = ?", (course_id,))
    moduleliste = cursor.fetchall()

    for module in moduleliste:
        module_id = module[1]
        cursor.execute("INSERT INTO studentoverview (student_id, module_id, module_status) VALUES (?,?,?)", (student_id, module_id, "offen"))

    cursor.execute("UPDATE student SET student_course = ?, student_semester=?, student_gradetarget=? WHERE student_id = ?", (course_id, student_semester, student_gradetarget, student_id))

    connection.commit()
    connection.close()
    print(f"{student_id} wurde in den Kurs {course_id} eingeschrieben.")


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


