import sqlite3

# --- Datenbank wird aufgesetzt ---

def start_databank():
    connection = sqlite3.connect("databank.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute(f"""
           CREATE TABLE IF NOT EXISTS student (
               id TEXT PRIMARY KEY NOT NULL,
               name TEXT NOT NULL,
               lastname TEXT NOT NULL
            )
           """)

    cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS course (
               id TEXT PRIMARY KEY NOT NULL,
               name TEXT NOT NULL,
               etc TEXT NOT NULL
            )
            """)

    cursor.execute(f"""
             CREATE TABLE IF NOT EXISTS module (
                id TEXT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                etc TEXT NOT NULL,
                status TEXT NOT NULL
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

    connection.commit()
    connection.close()

