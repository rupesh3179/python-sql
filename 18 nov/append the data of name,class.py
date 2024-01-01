x=int(input("how many studeny detail you want to enter:"))
file=open("student2.txt","a")

for i in range(x):
    name=input("enter students name:")
    clas=int(input("enter your class:"))
    record=name+" "+str(clas)+"\n"
    print(record)
    file.write(record)
file.close()