import sqlite3
from data.add_to_database import new_modul_db, new_course_db, add_modules_to_course

# ---DB: Funktionen, um die Datenbank initial aufzusetzen und initiale Daten einzufügen.---

def start_databank():
    """Die Datenbank wird initial aufgesetzt.
    Es werden die Tabellen Student, Course, Module, Course-Module, StudentenOverview erstellt."""

    connection = sqlite3.connect("databank.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute(f"""
           CREATE TABLE IF NOT EXISTS student (
               student_id TEXT PRIMARY KEY NOT NULL,
               student_name TEXT NOT NULL,
               student_lastname TEXT NOT NULL,
               student_course TEXT REFERENCES course(course_id) ON DELETE RESTRICT,
               student_semester INT
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
             CREATE TABLE IF NOT EXISTS modules (
                module_id TEXT PRIMARY KEY NOT NULL,
                module_name TEXT NOT NULL UNIQUE,
                module_etc INT NOT NULL
             )
             """)
    cursor.execute(f"""
             CREATE TABLE IF NOT EXISTS course_modules (
                course_id TEXT NOT NULL REFERENCES course(course_id) ON DELETE RESTRICT,
                module_id TEXT NOT NULL REFERENCES modules(module_id) ON DELETE RESTRICT,
                position INTEGER,
                PRIMARY KEY (course_id, module_id)
             )
             """)

    cursor.execute(f"""
             CREATE TABLE IF NOT EXISTS studentoverview (
                student_id TEXT NOT NULL REFERENCES student(student_id) ON DELETE RESTRICT,
                module_id TEXT NOT NULL REFERENCES modules(module_id) ON DELETE RESTRICT,
                module_status TEXT NOT NULL,
                module_grade INTEGER, 
                PRIMARY KEY (student_id, module_id)
             )
             """)

    connection.commit()
    connection.close()

def insert_moduledata_db():
    """ Initiale Daten für Module werden eingelesen."""
    with open ("module.csv", "r", encoding="utf-8") as moduleliste:
        for line in moduleliste:
            module = line.strip().strip('"').split(", ")
            module_id = module[0]
            module_name = module[1]
            module_etc = module[2]
            print(module_id, module_name, module_etc)

            new_modul_db(module_id, module_name, module_etc)

def insert_coursedata_db():
    """Initiale Daten für Course werden eingelesen."""
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
    """Initial wird ein Kurs mit Modulen verbunden"""
    with open ("module.csv", "r", encoding="utf-8") as moduleliste:
        for line in moduleliste:
            module = line.strip().strip('"').split(", ")
            module_id = module[0]

            add_modules_to_course("FS-BAAKI-01", module_id)

