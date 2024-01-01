import mysql.connector as c
con=c.connect(host="localhost",user="root",password=input(""),database="python")
cursor=con.cursor()
dcode=int(input("ender dcode:"))
dname=input("")
HOD=input("")
query="insert into values({},'{}',{})".format(dcode,dname,HOD)
cursor.execute(query)
con.commit()




import mysql.connector as c
con=c.connect 



















import my