import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="anisole@3179",database="python")
cursor=con.cursor()
while True:
    First_Name=input("Enter first name: ")
    Last_Name=input("Enter second name: ")
    query="Insert into name values('{}','{}')".format(First_Name,Last_Name)
    cursor.execute(query)
    con.commit()
    print("data entered successfully")
    x=
