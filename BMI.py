weight=int(input("enter your weight in kg:"))
height=int(input("enter your height in cm:"))

bmi=weight/(height/100)**2

if bmi<18.4:
    print("you are under weight")

elif bmi<24.9:
    print("you are healthy")

elif bmi<29.9:
    print("you are over weight")

else:
    print("you are severely obese")