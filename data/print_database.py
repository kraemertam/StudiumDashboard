import sqlite3


def print_databank():
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student")
    print("Studenten:")
    for row in cursor.fetchall():
        print(row)
    cursor.execute("SELECT * FROM modules")
    print("Module:")
    for row in cursor.fetchall():
        print(row)
    cursor.execute("SELECT * FROM course")
    print("Kurse:")
    for row in cursor.fetchall():
        print(row)
    cursor.execute("SELECT * FROM course_modules")
    print("Zuordnung:")
    for row in cursor.fetchall():
        print(row)
    cursor.execute("SELECT * FROM studentoverview")
    print("Übersicht Studenten:")
    for row in cursor.fetchall():
        print(row)

    connection.close()
