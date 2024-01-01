# def fib(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     else:
#         return fib(n-2)+fib(n-1)

# n=int(input("enter number:"))
# for i in range(1,n):
#     print(fib(i),end=' ')

def push(item,stk):
    stk.append(item)
    return item
def pop(item):
    item=stk.pop()
    return item
def peek():
    top=len(stk)-1
    return stk[top]
def display():
    top=len(stk)-1
    for i in range(top,-1,-1):
        print(stk[a],end=' ')
        print()
stack=[]
ch=int(input("enter any number:"))
while True:
    if ch==1:
        item

    
