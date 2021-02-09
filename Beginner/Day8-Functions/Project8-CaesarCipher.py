"""Caesar cipher."""

import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

contin = True


def caesar(start_text, shift_amount, cipher_direction):
    """Caesar function."""
    end_text = ""
    shift = (shift_amount % 26)
    if cipher_direction == "decode":
        shift *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                end_text += alphabet[new_position]
            else:
                end_text += char
                print(f"Here's the {cipher_direction}d result: {end_text}\n")


print(art.logo)

while contin:

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    Want_to_continue = input("Do you want to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if Want_to_continue == "no":
        contin = False
        print("Goodbye")
