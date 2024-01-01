def Push(stk,item):
    stk.append(item)
def Pop(stk):
    item=stk.pop()
    return item
def Peek(stk):
    top=len(stk)-1
    return stk[top]
def Display(stk):
    top=len(stk)-1    
    for a in range(top,-1,-1):
        print(stk[a],end=" ")
    print()

Stack=[]
while True:
    print("1 to 5")
    ch=int(input("->"))
    if ch==1:
        item=int(input("enter item:"))
        Push(Stack,item)
    elif ch==2:
        item=Pop(Stack)
        print(item)
    elif ch==3:
        item=Peek(Stack)
        print(item)
    elif ch==4:
        Display(Stack)
    elif ch==5:
        break
    else:
        print("invalid choice")










