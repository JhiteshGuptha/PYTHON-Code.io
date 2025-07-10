# Number Guessing Game in Python

import random

start = 1
end = 10
guessNumber = random.randint(start, end)
wrongGuess = 0
isRunning = True

print("----------Welcome to the Game----------\n")
while isRunning:
    guessInput = int(input(f"Guess a Number between {start} & {end}: "))

    if guessInput < start or guessInput > end:
        print("Enter a Number within Range 😐")
    elif guessInput < guessNumber:
        print(f"{guessInput} is Less than the Number 🤨")
        wrongGuess += 1
        print(f"Wrong Guesses: {wrongGuess}")
    elif guessInput > guessNumber:
        print(f"{guessInput} is Greater than the Number 🤕")
        wrongGuess += 1
        print(f"Wrong Guesses: {wrongGuess}")
    else:
        print("-----------------------------------")
        print(f"{guessInput} is the Right Guess 🥳")
        print(f"Number of Guesses: {wrongGuess + 1}")
        isRunning = False
