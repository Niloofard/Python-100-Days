import string


def encrypt(plain_text, shift):
    plain_text = plain_text.lower()
    cipher_text =""
    alphabet = string.ascii_lowercase
    print(alphabet)
    for char in plain_text:
        if char.isalpha():
            cipher_text += alphabet [alphabet.index(char)+shift]
        else:
            cipher_text +=char
    print(cipher_text)


def decrypt(cipher_text, shift):
    cipher_text = cipher_text.lower()
    alphabet = string.ascii_lowercase
    plain_text=""
    for char in cipher_text:
        if char.isalpha():
            plain_text +=alphabet[alphabet.index(char)-shift]
        else:
            plain_text +=char
    print(plain_text)

user_input = input("Type Encode to Encrypt or Decode to Decrypt:")
if user_input== "Encode":
    message = input("Type Your Message:")
    shift = int(input("Type the Shift Number:"))
    encrypt(message, shift)
else:
    message = input("Type Your Message:")
    shift = int(input("Type the Shift Number:"))
    decrypt(message, shift)