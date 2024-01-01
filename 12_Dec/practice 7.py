import mysql.connector as c
con=c.connect(host="localhost",user="root",password="anisole@3179",database="python")
cursor=con.cursor()
cursor.execute("select * from biodata")
for i in range(cursor.rowcount):
    data=cursor.fetchone()
    print(data) 


    
    







