def gp(a, r):
    if 0<=r<1:
        return a/(1-r)
    else:
        print("put r in range of 0 and 1")

a = int(input("enter any number: "))
r = float(input("enter a number: "))
z = gp(a, r)
print("the sum of the numbers from 1 to", a, "is", z)
