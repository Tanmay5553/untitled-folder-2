import random

random_number =random.randint(1,10)

while True:
    user_guess = int(input("guess number(1-10): "))

    if random_number == user_guess:
        print("congratulations you have guessed it right!")
        break

    elif user_guess< random_number:
        print("guess higher number")

    else:
        print("guess lower number")