import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE users (id int, username text, password text)")

cursor.executemany("INSERT INTO users VALUES (?, ?, ?)",
                   [(1, "TESTE", "TESTE"), (2, "TESTE", "TESTE"), (3, "TESTE", "TESTE")])


rows = cursor.execute("SELECT * FROM users")

for row in rows:
    print(row)

connection.commit()

connection.close()
