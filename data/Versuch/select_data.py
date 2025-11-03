import sqlite3

def select_student_db():
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * from student")
    for row in cursor.fetchall():
        print(row)

    connection.commit()
    connection.close()


select_student_db()
