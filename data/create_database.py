import sqlite3
from add_to_database import new_modul_db

from data.add_to_database import new_modul_db, new_course_db, add_modules_to_course


# --- Datenbank wird aufgesetzt ---

def start_databank():
    connection = sqlite3.connect("databank.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute(f"""
           CREATE TABLE IF NOT EXISTS student (
               student_id TEXT PRIMARY KEY NOT NULL,
               student_name TEXT NOT NULL,
               student_lastname TEXT NOT NULL
            )
           """)

    cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS course (
               course_id TEXT PRIMARY KEY NOT NULL,
               course_name TEXT NOT NULL,
               course_title TEXT NOT NULL,
               course_etc INTEGER NOT NULL
            )
            """)

    cursor.execute(f"""
             CREATE TABLE IF NOT EXISTS module (
                module_id TEXT PRIMARY KEY NOT NULL,
                module_name TEXT NOT NULL,
                module_etc TEXT NOT NULL
             )
             """)
    cursor.execute(f"""
             CREATE TABLE IF NOT EXISTS course_modules (
                course_id TEXT NOT NULL REFERENCES course(id) ON DELETE CASCADE,
                module_id TEXT NOT NULL REFERENCES module(id) ON DELETE RESTRICT,
                position INTEGER,
                PRIMARY KEY (course_id, module_id)
             )
             """)

    cursor.execute(f"""
             CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id INTEGER PRIMARY KEY,
                student_id TEXT NOT NULL REFERENCES student(id) ON DELETE CASCADE,
                course_id TEXT NOT NULL REFERENCES course(id) ON DELETE CASCADE,
                UNIQUE (student_id, course_id)
             )
             """)

    cursor.execute(f"""
             CREATE TABLE IF NOT EXISTS studentoverview (
                student_id TEXT NOT NULL REFERENCES student(id),
                module_id TEXT NOT NULL REFERENCES module(id) ON DELETE CASCADE,
                module_name TEXT NOT NULL REFERENCES module(name) ON DELETE CASCADE,
                module_status TEXT NOT NULL,
                module_grade INTEGER, 
                PRIMARY KEY (student_id, module_id)
             )
             """)

    connection.commit()
    connection.close()

def insert_moduledata_db():
    with open ("module.csv", "r", encoding="utf-8") as moduleliste:
        for line in moduleliste:
            module = line.strip().strip('"').split(", ")
            module_id = module[0]
            module_name = module[1]
            module_etc = module[2]
            print(module_id, module_name, module_etc)

            new_modul_db(module_id, module_name, module_etc)

def insert_coursedata_db():
    with open ("course.csv", "r", encoding="utf-8") as courselist:
        for line in courselist:
            course = line.strip().strip('"').split(", ")
            course_id = course[0]
            course_name = course[1]
            course_title = course[2]
            course_etc = course[3]
            print(course_id, course_name, course_title, course_etc)

            new_course_db(course_id, course_name, course_title, course_etc)

def initialize_course():
    with open ("module.csv", "r", encoding="utf-8") as moduleliste:
        for line in moduleliste:
            module = line.strip().strip('"').split(", ")
            module_id = module[0]

            add_modules_to_course("FS-BAAKI-01", module_id)

