import random 

choices = ["rock","paper","scissor"]

while True:
    print("1.rock\n2.paper\n3.scissor\n4.exit")
    user_ch=input("enter your choice : ").strip().lower()

    if user_ch=="exit":
        print("thanks for playing game")
        break

    computer_ch=random.choice(choices)
    print("user choice:",user_ch)
    print("computer choice:",computer_ch)
    if user_ch==computer_ch:
        print("its a tie")

    elif(user_ch=="rock"and computer_ch=="scissor")or(user_ch=="paper"and computer_ch=="rock")or(user_ch=="scissor"and computer_ch=="paper"):
        print("user wins")

    else:
        print("computer wins")





