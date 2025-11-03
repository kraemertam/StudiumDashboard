import sqlite3

# --- Neue Studenten, Kurse, Module werden angelegt ---

def new_student_db(id, name, lastname):
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO student (id, name, lastname) VALUES (?,?,?)", (id, name, lastname))
    connection.commit()
    connection.close()
    print("Student wurde angelegt.")


def new_modul_db(id, name, etc, status):
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO module (id, name, etc, status) VALUES (?,?,?,?)", (id, name, etc, status))
    connection.commit()
    connection.close()
    print("Modul wurde angelegt.")


def new_course_db(id, name, etc):
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO course (id, name, etc) VALUES (?,?,?)", (id, name, etc))
    connection.commit()
    connection.close()
    print("Course wurde angelegt.")

def add_modules_to_course(course_id, module_id):
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO course_modules (course_id, module_id) VALUES (?,?)", (course_id, module_id))
    connection.commit()
    connection.close()
    print("Das Modul wurde dem Kurs hinzugefügt.")

