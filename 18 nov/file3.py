number=int(input("enter any number:"))
print(f"multiplication table for {number} is:")

for i in range(1,11):
    result = number*i
    print(f"{number} X {i} = {result}")
