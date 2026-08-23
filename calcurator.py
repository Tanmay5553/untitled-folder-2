def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2

print("which operation to select: ")

print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")

ch=input("enter the option:")
num1=int(input("enter the first value:"))
num2=int(input("enter the second value:"))
if ch=="1":
    print("addition of :","num1","and","num2","is",addition(num1,num2))
elif ch=="2":
    print("substraction of :","num1","and","num2","is",subtraction(num1,num2))
elif ch=="3":
    print("multiplication of :","num1","and","num2","is",multiplication(num1,num2))
elif ch=="4":
    print("division of :","num1","and","num2","is",division(num1,num2)) 

else:
    print("invalid input")