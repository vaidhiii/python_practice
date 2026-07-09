import random

guess = random.randint(1, 50)
print(guess)
while True:
    num = int(input("Guess a Number From 1 to 50: "))
    if num < 1 or num > 50:
        print("Guess within range.")
    elif guess == num:
        print("Your Guess is Correct.")
        break
    elif num > guess:
        print("You Guessed Too High.")
    elif guess > num:
        print("You Guessed Too Low.")
