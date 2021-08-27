import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
cur.execute("SELECT * FROM student")
row = cur.fetchone()
print(row)
con.close()
