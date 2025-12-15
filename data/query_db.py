import sqlite3
from pathlib import Path

# --- Database Queries -----------------------------------------------------------------------------------------------

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
    if student[3] == None:
        course_name = None
        course_etc = None
    else:
        cursor.execute("SELECT course_name, course_etc from course WHERE course_id = ?", (student[3],))
        course_info = cursor.fetchone()
        course_name = course_info[0]
        course_etc = course_info[1]
    connection.close()
    print(student_id, student_name, student_lastname, student_course, course_name, course_etc, student_semester)
    return student_id, student_name, student_lastname, student_course, course_name, course_etc, student_semester


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