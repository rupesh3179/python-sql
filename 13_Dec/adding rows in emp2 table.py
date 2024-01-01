import mysql.connector as c
con=c.connect(host="localhost",user="root",password=input(""),database="rupesh")
cursor=con.cursor()
while True:
    code=int(input("Enter Code: "))
    name=input("Enter name: ")
    salary=int(input("Enter salary:"))
    query="Insert into emp2 values({},'{}',{})".format(code,name,salary)
    cursor.execute(query)
    con.commit()
    print("Data inserted successfully")
    x=int(input("1) for more\n2) for exit\n:"))
    if x==1:
        print("Ok then continue:")
    else:
        break
