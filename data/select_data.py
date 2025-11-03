import sqlite3

def select_student_db():
    connection = sqlite3.connect("databank.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * from student")
    for row in cursor.fetchall():
        print(row)

    connection.commit()
    connection.close()


#select_student_db()

def select():
    connection = sqlite3.connect("databank.db")
    c = connection.cursor()
    c.execute("SELECT * from student WHERE lastname = 'Krämer'")
    #print(c.fetchone()) # nur das eine Element
    print(c.fetchall()) # Liste mit allen Elementen, die zur Anfrage passen

select()

