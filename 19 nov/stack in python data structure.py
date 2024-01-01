def push(a,val):
    a.append(val)
def pop(a):
    item=a.pop()
    print("popped item",item)
def peak():
    last=len(a)-1
    print("peak element",a[last])
def display(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])
#___main___
a=[]
while True:
    choice=int(input("1) ->Push\n2) -Ppop\n3) ->Peak4) ->Display\n5) ->Exit\nEnter Your Choice"))
    if choice==1:
        val=int(input("enter number to insert"))
        push(a,val)
        print("element pushed successfullt")
    elif choice==2:
        pop(a)
    elif choice==3:
        peak(a)
    elif choice==4:
        display(a)
    else:
        break