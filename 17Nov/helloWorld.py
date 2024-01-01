number = int(input("Enter any number: "))
print(f"Multiplication table for {number} is:")

for i in range(1, 11):
    result = number * i
    print(f"{number} X {i} = {result}")
