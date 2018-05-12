#!/usr/bin/env python
import cgi,sqlite3
print("Content-type:text/html \n")
form=cgi.FieldStorage()
a=form.getvalue("sid")
conn=sqlite3.connect("vishnu.db")
cur=conn.cursor()
sql="delete from student1 where id="+a
try:
    cur.execute(sql)
    conn.commit()
    print("deleted successfully")
except Exception as e:
    print(e)
cur.close()
conn.close()
