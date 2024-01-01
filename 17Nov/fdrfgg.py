def push(stk,item):
    stk.append(item)
def pop(item):
    item=stk.pop()
    return item
def peek(stk):
    top=len(stk)-1
    return stk[top]


Stack=[]
while True:
    ch=int(input("enter from 1 to 5"))
    if ch==1:
        item=int(input("enter item"))
        push(stack,item)
    elif ch==2:
        item=pop(stack)
        return item
    elif ch==3:
        item=peek(stack)
        return item
    elif ch==4:
        display(stack)
    elif ch==5:
        break
    else:
        print("invalid successfully")
    