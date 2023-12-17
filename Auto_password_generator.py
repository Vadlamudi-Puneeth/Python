import random

alphabets = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
symbols = ['!','@','#','$','%','^','&','*','(',')']
numbers = ['1','2','3','4','5','6','7','8','9','0']

print("Welcome to password generator \n")

alphabets_range = int(input("How many letters do u want?: "))
symbols_range = int(input("How many symbols do u want?: "))
numbers_range = int(input("How many numbers do u want?: "))


password_list = []

for i in range(alphabets_range):
    random_alphabets = random.choice(alphabets)
    password_list += random_alphabets

for i in range(symbols_range):
    random_symbols = random.choice(symbols)
    password_list += random_symbols

for i in range(numbers_range):
    random_numbers = random.choice(numbers)
    password_list += random_numbers

random.shuffle(password_list)
print("password in the form of list")
print(password_list)

my_password = ''.join(password_list)
print("\nFinal password")
print(my_password)
