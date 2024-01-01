import random
play1=input("enter player name 1:")
play2=input("enter player name 2:")
play3=input("enter player name 3:")

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Print the random number
a=print("Random Number:", random_number)
b=print("Random Number:", random_number)
c=print("Random Number:", random_number)
if a>b:
    if b>c:
        print(f("{play1} won\n{play3} loose"))
    else:
        print(f("{play1} won\n{play2} loose"))
if b>a:
    if a>c:
        print(f("{play2} won\n{play3} loose"))
    else:
        print(f("{play2} won\n{play1} loose"))
if c>a:
    if a>b:
        print(f("{play3} won\n{play2} loose"))
    else:
        print(f("{play3} won\n{play1} loose"))