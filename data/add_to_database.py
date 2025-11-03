import sqlite3

# --- Neue Studenten, Kurse, Module werden angelegt ---

def new_student_db(student_id, student_name, student_lastname):
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO student (student_id, student_name, student_lastname) VALUES (?,?,?)", (student_id, student_name, student_lastname))
    connection.commit()
    connection.close()
    print("Student wurde angelegt.")


def new_modul_db(module_id, module_name, module_etc):
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO module (module_id, module_name, module_etc) VALUES (?,?,?)", (module_id, module_name, module_etc))
    connection.commit()
    connection.close()
    print("Modul wurde angelegt.")


def new_course_db(course_id, course_name, course_title, course_etc):
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO course (course_id, course_name, course_title, course_etc) VALUES (?,?,?,?)", (course_id, course_name, course_title, course_etc))
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

#def enroll_course(student_id, course_id):
    #connection = sqlite3.connect("databank.db")
    #cursor = connection.cursor()
    #cursor.execute("SELECT modul_id FROM course_modules")
    #cursor.fetchall()
    #for modul in cursor.fetchall():
    #    print(modul)

   # cursor.execute("INSERT INTO studentoverview (student_id, module_id) VALUES (?,?)", (course_id, module_id))
    #connection.commit()
    #connection.close()
    #print("Das Modul wurde dem Kurs hinzugefügt.")

#enroll_course()