age=int(input("enter your age: "))

if age>=18:
    print("you are adult and between 10 to 20 years old")

elif age<10:
    print("you are not an adult and less than 10 years old")

elif age<20 and age>10:
    print("you are between 10 to 20 years old a healthy teenager")

elif age>20 and age<30:
    print("you are not a teenager and you are above 20 years old")

else:
    print("you are old")

