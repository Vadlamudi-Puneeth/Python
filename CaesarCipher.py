alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def Encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char
    print(f"Here's the text after encryption: {cipher_text}")

def Decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabets[new_position]
        else:
            plain_text += char
    print(f"Here's the text after decryption: {plain_text}")

want_to_end = False

while not want_to_end:
    what_to_do = input("Enter 'encrypt' for encryption and 'decrypt' for decryption: ")
    text = input("Enter the word that you want to shift: ")
    key = int(input("Enter the shift key (how many times do you want to shift?): "))

    if what_to_do == "encrypt":
        Encryption(text, key)
    elif what_to_do == "decrypt":
        Decryption(text, key)

    play_again = input("Type 'yes' if you want to play again, otherwise type 'no': ")

    if play_again.lower() == "no":
        want_to_end = True
        print("Have a nice day! Goodbye!")
