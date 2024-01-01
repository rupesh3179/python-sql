import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="anisole@3179",database="rupesh")
cursor=con.cursor()
code=int(input("Enter Employee Code:"))
query="delete from emp2 where code={}".format(code)
cursor.execute(query)
con.commit()
if cursor.rowcount>0:
    print("Deletion successfully")
else:
    print("Employee code not found")