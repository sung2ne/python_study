import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
cur.execute("SELECT * FROM student")
rows = cur.fetchmany(3)

for row in rows:
    print(row)

con.close()
