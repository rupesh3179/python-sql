import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="anisole@3179",database="rupesh")
cursor=con.cursor()
code=int(input("Enter Employee Code:"))
salary=int(input("Enter new salary:"))
query="update emp2 set salary={} where code={}".format(salary,code)
cursor.execute(query)
con.commit()
if cursor.rowcount>0:
    print("Data updated successfully")
else:
    print("NO Data Found.")