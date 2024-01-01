import mysql.connector as c

con = c.connect(host="localhost", user="root", password="anisole@3179", database="python")
cursor = con.cursor()

while True:
    code = int(input("code:"))
    name = input("name:")
    salary = int(input("salary:"))
    dcode = int(input("dcode:"))
    updated_salary = int(input("upd salary:"))

    # Inserting data
    query1 = "insert into emp values({},'{}',{},{})".format(code, name, salary, dcode)
    cursor.execute(query1)

    # Updating salary
    query2 = "update emp set salary={} where code={}".format(updated_salary, code)
    cursor.execute(query2)

    con.commit()
    print("data entered successfully:")
    x = int(input("enter 1 for continue\nenter 2 for close"))
    if x == 1:
        continue
    else:
        break
