import sqlite3

con = sqlite3.connect("test.db")

cur = con.cursor()
sql = "INSERT INTO student (name, phone, address) values (?, ?, ?)"
cur.executemany(sql, [
    ("고길동", "010-1235-5778", "경기"),
    ("김길동", "010-1236-5878", "강원도"),
    ("최길동", "010-1237-5978", "부산"),
    ("이길동", "010-1238-5628", "대전")
])
con.commit()

con.close
