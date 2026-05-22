"""This file is for printing the DB."""

import sqlite3
from pathlib import Path


def print_databank():
    db_path = Path(__file__).resolve().parent / "databank.db"
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
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

print_databank()