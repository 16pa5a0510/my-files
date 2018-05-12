#!/usr/bin/env python
import cgi,sqlite3
print("Content-type:text/html \n")
form=cgi.FieldStorage()
a=form.getvalue("sid")
b=form.getvalue("sname")
c=form.getvalue("semail")
d=form.getvalue("scontact")
conn=sqlite3.connect("vishnu.db")
cur=conn.cursor()
sql="update student1 set name='"+b+"',email='"+c+"',contact='"+d+"' where id="+a
try:
    cur.execute(sql)
    conn.commit()
    print("updated successfully")
    print("<meta http-equiv=\"refresh\"content=\"0;url=http://localhost:5555/home.html\"/>")
except Exception as e:
    print(e)
cur.close()
conn.close()
