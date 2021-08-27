import sqlite3

con = sqlite3.connect("test.db")

cur = con.cursor()
sql = "INSERT INTO student (name, phone, address) values (?, ?, ?)"
cur.execute(sql, ("홍길동", "010-1234-5678", "서울"))
con.commit()

con.close
