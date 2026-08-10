"""This file is for creating the database."""
import sqlite3
from pathlib import Path

def start_databank():
    """The database is set up initially.
    The tables student, course, module, course_modules and studentoverview are created."""
    
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute(f"""
           CREATE TABLE IF NOT EXISTS student (
               student_id TEXT PRIMARY KEY NOT NULL,
               student_name TEXT NOT NULL,
               student_lastname TEXT NOT NULL,
               student_course TEXT REFERENCES course(course_id) ON DELETE RESTRICT,
               student_semester INT,
               student_gradetarget FLOAT
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
                module_grade REAL, 
                PRIMARY KEY (student_id, module_id)
             )
             """)

    connection.commit()
    connection.close()

