#!/usr/bin/env python
import cgi,sqlite3
print("Content-type:text/html \n")
form=cgi.FieldStorage()
a=form.getvalue("email")
b=form.getvalue("password")
conn=sqlite3.connect("vishnu.db")
cur=conn.cursor()
sql="select * from student where email=='"+a+"' and password='"+b+"'"
c=cur.execute(sql)
rs=c.fetchall()
if (len(rs)>0):
	print("login successfully")
	print("<meta http-equiv=\"refresh\"content=\"0;url=http://localhost:5555/home.html\"/>")
else:
	print("login failure")
cur.close()
conn.close()
