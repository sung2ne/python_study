import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
sql = "SELECT * FROM student WHERE name == ?"
cur.execute(sql, ("홍길동",))
rows = cur.fetchall()

for row in rows:
    print(row)

con.close()
