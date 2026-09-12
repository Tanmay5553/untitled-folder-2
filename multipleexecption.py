print("code before try")

try:
    num1=int(input("Enter a number: "))
    print(num1/0)
    print("extra code in try")
except ValueError:
    print("handled the exception")
except ZeroDivisionError:
    print("handled the exception")
except:
    print("handled the exception")


print("code after try")
