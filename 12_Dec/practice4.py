# Guess the number game using a while loop

import random

target_number = random.randint(1, 100)
guess = None
attempts = 0

while guess== target_number:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1

    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
