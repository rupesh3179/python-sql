import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd=input(""),database="python")
cursor=con.cursor()
while True:
    First_Name=input("Enter first name: ")
    Last_Name=input("Enter second name: ")
    query="Insert into name values('{}','{}')".format(First_Name,Last_Name)
    cursor.execute(query)
    con.commit()
    print("Data inserted successfully")
    x=int(input("1) for more\n2) for exit\n:"))
    if x==1:
        print("Ok then continue:")
    else:
        break





