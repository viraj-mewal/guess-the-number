# Guess the number

import random

comp_guess = random.randint(1, 20)
turns = 1

while True:
    guess = int(input("Enter your guess (1-20) :-"))
    if guess == comp_guess:
        break
    else:
        if guess > comp_guess:
            print("Lower guess please !")
        else:
            print("Higher guess please")
        turns += 1

print("You guessed it in", str(turns))

# completed