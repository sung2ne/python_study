import sqlite3

con = sqlite3.connect("test.db")

cur = con.cursor()
sql = "UPDATE student SET name = ? WHERE id = ?"
cur.execute(sql, ("최민수", 1))
con.commit()

con.close
