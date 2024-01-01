try:
    
    num1=int(input("enter any number"))
    num2=int(input("enter any number"))
    print(num1/num2)

except ZeroDivisionError:
    print("error: division by 0 is not allowed:")
except ValueError:
    print("enter numberic value")
finally:
    print("program execution completed")
