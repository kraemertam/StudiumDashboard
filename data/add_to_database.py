import sqlite3

# ---DB: In dieser Datei befinden sich die Funktionen, um neue Studenten, Kurse, Module und der Verbindungen in der Datenbank anzulegen. ---

def new_student_db(student_id: str, student_name: str, student_lastname: str):
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO student (student_id, student_name, student_lastname) VALUES (?,?,?)", (student_id, student_name, student_lastname))
    connection.commit()
    connection.close()
    print("Student wurde angelegt.")


def new_modul_db(module_id: str, module_name: str, module_etc: int):
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO module (module_id, module_name, module_etc) VALUES (?,?,?)", (module_id, module_name, module_etc))
    connection.commit()
    connection.close()
    print("Modul wurde angelegt.")


def new_course_db(course_id: str, course_name: str, course_title: str, course_etc: int):
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO course (course_id, course_name, course_title, course_etc) VALUES (?,?,?,?)", (course_id, course_name, course_title, course_etc))
    connection.commit()
    connection.close()
    print("Course wurde angelegt.")

def add_modules_to_course(course_id: str, module_id: str):
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO course_modules (course_id, module_id) VALUES (?,?)", (course_id, module_id))
    connection.commit()
    connection.close()
    print("Das Modul wurde dem Kurs hinzugefügt.")
