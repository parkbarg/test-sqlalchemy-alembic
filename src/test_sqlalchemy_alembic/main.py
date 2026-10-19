import sqlite3

connection = sqlite3.connect("test.db")

connection.execute(
    "INSERT INTO users (name) VALUES (?)",
    ("Taro",),
)

connection.commit()

rows = connection.execute(
    "SELECT * FROM users"
).fetchall()

print(rows)

connection.close()
