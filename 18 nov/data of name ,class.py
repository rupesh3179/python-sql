x=int(input("how many studeny detail you want to enter:"))
file=open("student2.txt","w")

for i in range(x):
    name=input("enter students name:")
    clas=int(input("enter your class:"))
    file.write(name+" "+str(clas)+"\n")
file.close()

