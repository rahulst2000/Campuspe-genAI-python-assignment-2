# The user gets limited chances to guess the number.
# The program shows if the guess is too high or too low.
# The game ends when the number is guessed or chances are over.

import random

num = random.randint(1, 100)
attempts = 5

for i in range(attempts):
    guess = int(input("Guess number (1-100): "))

    if guess == num:
        print("Correct!")
        break
    elif guess < num:
        print("Too low.")
    else:
        print("Too high.")
else:
    print("No attempts left. Number was:", num)