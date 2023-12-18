import random

my_list = ['apple','mango','grapes']
random_item = random.choice(my_list)
print(random_item)
lives = len(random_item)+1

empty_list = []
for letter in random_item:
    empty_list+="_"
print(empty_list)

game_over = False

while(not game_over):
    user_input = input("Guess the letter: \n")
    
    for position in range(len(random_item)):
        letter = random_item[position]
        if (letter == user_input):
            empty_list[position] = user_input
    print(empty_list)
    
    if (user_input not in random_item):
        lives = lives - 1
        
        if(lives == 0):
            game_over = True
            print("\nyou lose\n")
            
    if "_" not in empty_list:
        game_over = True
        print("\nyou win\n")
