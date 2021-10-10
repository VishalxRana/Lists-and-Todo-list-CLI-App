import string 

# alphabet = string.ascii_lowercase
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_key, cipher_command):
    # For key higher than 26. In thousands or hundreds of thousands. 
    while shift_key > 26:
        shift_key -= 26
        if shift_key <= 26:
            break
    output = ""
    if cipher_command == "decode":
        shift_key *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_key
            output += alphabet[new_position]
        else: 
            output += char
    print(f"The {cipher_command}d text is {output}")

while True:
    command = input("Type 'encode' to encrpyt, type 'decode' to decrypt: ")
    text = input("Enter the text: ").strip().lower()
    key = int(input("Enter a number (key): "))

    caesar(start_text=text, shift_key=key, cipher_command=command)
    
    result = input("Do you wanna continue? y/n: ")
    if result == 'n':
        print("Alright, see you later alligator!")
        break
        
