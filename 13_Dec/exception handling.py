try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    d=a/b
    print(d)
except ValueError:
    print("please enter valid number:")
except ZeroDivisionError:
    print("cant divide by 0")
finally:
    print("this block always executes:")