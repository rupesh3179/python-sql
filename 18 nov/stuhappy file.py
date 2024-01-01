myfile=open("stuhappy.txt","w")
for i in range(3):
    name=input("enter your name:")
    myfile.write(name)
    myfile.write('\n')
myfile.close()
