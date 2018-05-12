#!/usr/bin/env python
import sqlite3,cgi
print("Content-type:text/html \n")

conn=sqlite3.connect("vishnu.db")
cur=conn.cursor()
sql="select * from student1"

html='''
<html>
<body>
<table border=2>
'''
print(html)
try:
    rs=cur.execute(sql)
except Exception as e:
    print(e)
else:
    for record in cur:
        print("<tr>")
        for column in record:
            print("<td>"+str(column)+"</td>")
        print("</tr>")
        html='''
</table>
</body>
</html>
'''
cur.close()
conn.close()
