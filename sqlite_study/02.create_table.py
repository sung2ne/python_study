import sqlite3

con = sqlite3.connect("test.db")

sql = """
CREATE TABLE student(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT, 
    phone TEXT, 
    address TEXT
)
"""

con.execute(sql)

con.close()
