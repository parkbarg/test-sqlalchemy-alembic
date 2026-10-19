import sqlite3

connection = sqlite3.connect("test.db")

connection.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
""")

connection.commit()
connection.close()
