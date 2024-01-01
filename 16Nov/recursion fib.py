# for i in range(1,5):
#     for j in range(1,11):
#         print(f"{i}X{j}={i*j}")
    

def fib(n):
    if n==2:
        return 1
    if n==1:
        return 0
    else:
        return fib(n-1) + fib(n-2)
    
n=int(input("enter any number:"))
for i in range(1,n+1):
    print(fib(i),end=', ')



