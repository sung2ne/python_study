import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
cur.execute("SELECT * FROM student")
rows = cur.fetchall()

for row in rows:
    print(row)

con.close()
