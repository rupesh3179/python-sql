import pickle
def write():
    f=open("myfile.dat","wb")
    lst=[ 'gola', 'kaju', 'kishmish', 'badam', 'pista']
    pickle.dump(lst,f)
    f.close()

def read():
  f=open("myfile.dat","rb")
    lst1=pickle.load(f)
    print(lst1)
    f.close()  
write()
read()
print("data run successfully")