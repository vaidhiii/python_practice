import random
import string

print("......Password Generator......")

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

length = int(input("Enter password length: "))

if length <= 0:
    print("Please enter a positive number.")
else:
    password = ""

    for i in range(length):
        password += random.choice(all_characters)

print("Generated Password: ", password)
