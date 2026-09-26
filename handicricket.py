import random 

choices = ["1","2","3","4","5","6","7"]

while True:
    print("1.1\n2.2\n3.3\n4.4\n5.5\n6.6\n7.exit")
    user_ch=input("enter your choice : ")

    if user_ch=="exit":
        print("thanks for playing game")
        break

    computer_ch=random.choice(choices)
    print("user choice:",user_ch)
    print("computer choice:",computer_ch)
    if user_ch==computer_ch:
        print("its a tie")

    elif(user_ch=="1"and computer_ch=="0")or(user_ch=="2"and computer_ch=="1")or(user_ch=="6"and computer_ch=="5"):
        print("user wins")

    else:
        print("computer wins")





