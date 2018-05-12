#!/usr/bin/env python
import cgi,sqlite3
print("Content-type:text/html \n")
form=cgi.FieldStorage()
a=form.getvalue("sid")
conn=sqlite3.connect("vishnu.db")
cur=conn.cursor()
sql="select * from student1 where id="+a
try:
    cur.execute(sql)
    conn.commit()
except Exception as e:
    print(e)
else:
    for record in cur:
        pass
    html='''<html>
    <body>
    <form action="update.py" method="post">
    <input type="text" value="{}" name="sid" required><br>
    <input type="text" value="{}" name="sname" required><br>
    <input type="email" value="{}" name="semail" required><br>
    <input type="number" value="{}" name="scontact" required><br>
    <input type="submit" value="UPDATE">
    </form>
    </body>
    </html>'''.format(str(record[0]),record[1],record[2],record[3])
    print(html)
finally:
    curr.close()
    conn.close()
