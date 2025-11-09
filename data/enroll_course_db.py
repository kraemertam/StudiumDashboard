import sqlite3

# ---DB: Ein Student wird in einen Studiengang(Course) eingeschrieben.---

def enroll_course(student_id, course_id, student_semester):
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM course_modules WHERE course_id = ?", (course_id,))
    moduleliste = cursor.fetchall()

    for module in moduleliste:
        module_id = module[1]
        print(module_id)
        cursor.execute("SELECT module_name FROM module WHERE module_id = ?", (module_id,))
        modulename = cursor.fetchone()
        module_name = modulename[0]
        print(module_name)

        cursor.execute("INSERT INTO studentoverview (student_id, module_id, module_name, module_status) VALUES (?,?,?,?)", (student_id, module_id, module_name, "offen"))

    cursor.execute("SELECT course_etc FROM course WHERE course_id = ?", (course_id, ))
    course_etc = cursor.fetchone()[0]
    cursor.execute("UPDATE student SET student_course = ?, student_etc = ?, student_semester=? WHERE student_id = ?", (course_id, course_etc, student_semester, student_id))

    connection.commit()
    connection.close()
    print(f"{student_id} wurde in den Kurs {course_id} eingeschrieben.")
