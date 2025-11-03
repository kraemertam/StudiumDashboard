import sqlite3

connection = sqlite3.connect("meine_datenbank.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS person(
    id INTEGER PRIMARY KEY,
    name TEXT,
    vorname TEXT,
    geburtstag TEXT
)
""")

connection.commit()

cursor.execute("INSERT INTO person (name, vorname, geburtstag) VALUES (?,?,?)", ("Maier", "Hans", "1994-01-30"))
connection.commit()

cursor.execute("SELECT * FROM person")
for row in cursor.fetchall():
    print(row)


connection.close()
