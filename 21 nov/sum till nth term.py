def sum(num):
    if num==1:
        return 1
    else:
        return(num+sum(num-1))



a=int(input("enter any number"))
z=sum(a)
print("the sum of the numbers from 1 to",a,"is",z)


