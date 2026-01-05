
import sqlite3
from pathlib import Path

# ---DB: STUDENT IS ENROLLED IN A COURSE-----------------------------------------------------------------------------

def enroll_course(student_id: str, course_id: str, student_semester: int):
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM course_modules WHERE course_id = ?", (course_id,))
    moduleliste = cursor.fetchall()

    for module in moduleliste:
        module_id = module[1]
        cursor.execute("INSERT INTO studentoverview (student_id, module_id, module_status) VALUES (?,?,?)", (student_id, module_id, "offen"))

    cursor.execute("UPDATE student SET student_course = ?, student_semester=? WHERE student_id = ?", (course_id, student_semester, student_id))

    connection.commit()
    connection.close()
    print(f"{student_id} wurde in den Kurs {course_id} eingeschrieben.")
