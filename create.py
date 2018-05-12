import sqlite3
conn=sqlite3.connect("vishnu.db")
cur=conn.cursor()
sql="create table student(username varchar,password varchar,email varchar,contact varchar,address varchar)"
cur.execute(sql)
print("create successfully")
cur.close()
conn.close()
