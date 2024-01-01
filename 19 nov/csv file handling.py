import csv
def create():
    with open("details.csv","w") as obj:  #obj acts pointer
        fobj=csv.writer(obj)
        obj.writerows(['roll','name','marks'])
        while True:
            roll=int(input("enter your roll"))
            name=input("enter your name:")
            marks=int(input("enter your marks"))
            record=[roll,name,marks]
            fobj.writerow(record)
            choice=int("1) for exit and 2) for continue")
            if choice==1:
                break
def display():
    with open("details.csv","r") as obj:
        fobj=csv.reader(obj)
        for i in fobj:
            print(i)
create()
display()

