#!/usr/bin/env python
import cgi,sqlite3
print("Content-type:text/html \n")
form=cgi.FieldStorage()
a=form.getvalue("username")
b=form.getvalue("password")
c=form.getvalue("email")
d=form.getvalue("contact")
e=form.getvalue("address")
conn=sqlite3.connect("vishnu.db")
cur=conn.cursor()
sql="insert into student values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"')"
try:
	cur.execute(sql)
	conn.commit()
	print("successfully inserted")

	print("<meta http-equiv=\"refresh\"content=\"0;url=http://localhost:5555/login.html\"/>")
except Exception as e:
	print(e)
cur.close()
conn.close()
