def product(num):
    if num==1:
        return 1
    else:
        return(num*product(num-1))



a=int(input("enter any number"))
z=sum(a)
print("the factorial of the numbers ",a,"is",z)