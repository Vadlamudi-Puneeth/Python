import random

user_choice = int(input("Enter your choice: "))

if ( user_choice < 3 ):
    computer_choice = random.randint(0,2)
    print(computer_choice)

    if(computer_choice == user_choice):
        print("Draw no one will won this match")

    elif(computer_choice == 0 and user_choice == 2):
        print("you lose")

    elif(user_choice == 0 and computer_choice == 2):
        print("computer lose")

    elif(computer_choice > user_choice):
        print("you will loose")

    elif(computer_choice < user_choice):
        print("computer will lose")

else:
    print("you have to enter valid input")
