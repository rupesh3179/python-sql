a=open("student2.txt","w")
for i in range(int(input("how many detail"))):
    name=input("enter name:")
    clas=int(input("enter class:"))
    a.write(name+" "+str(clas)+"\n")
a.close()