import pickle
def write():
    s=open("myfile1.dat","wb")
    record=[]
    while True:
        roll=int(input("enter roll no."))
        name=input("enter your name:")
        marks=int(input("enter marks "))
        lst1=[roll,name,marks]
        record.append(lst1)
        choice=input("enter more records(y/n)")
        if choice=='n':
            break
            continue    
    pickle.dump(record,s)
    print("data run successfully")

def read():
    s=open("myfile1.dat","rb")
    r=pickle.load(s)
    print(r)
    for i in r:
        print(i)

def search():
    s=open("myfile1.dat","rb")
    roll=int(input("enter roll to search"))
    r=pickle.load(s)
    for i in r:
        if i[0]==roll:
            print(i)
            flag=1
            break
    if flag==0:
        print("numbe rot found")

write()
read()
search()
print("data run successfully")