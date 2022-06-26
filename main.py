import math
from .art import logo
print(logo)

is_Finished = False

while not is_Finished:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    def ciphor(text, shift, direction):
        ciphor = ""
        for letter in text:
            if letter in alphabet:
                if direction == "encode":
                    ind = alphabet.index(letter) + shift
                elif direction == "decode":
                    ind = alphabet.index(letter) - shift
                    if ind < 0:
                        ind = 26 + ind
                ciphor += alphabet[ind]
            else:
                ciphor += letter
        print(f"The {direction}d code is {ciphor}")

    ciphor(text, shift, direction)
    tex = input("Do you need to 'encode' or 'decode' .Type 'yes' or else 'no' .")
    if (tex == "no"):
        is_Finished = True
        print("Good Bye")
        print("\n\n\t\t Press any key to exit...")
    else:
        is_Finished = False
