medical_cause=input("enter the medical cause(y/n):")
if medical_cause=="y":
    print("you are allowed for exam")


else:
    attendance=int(input("enter your attendance : "))
    if attendance>=75:
        print("you are allowed")

    else:
        print("you are not allowded for exam")
          