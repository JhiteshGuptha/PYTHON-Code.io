# Rock, Paper and Scissor Game using Pythong

import random

options = ("Rock", "Paper", "Scissors")
isCorrect = True
computerPoints = 0
playerPoints = 0

print("-----Rock, Paper, Scissors Game, First to 3 points wins-----\n")
while isCorrect:
    computer = random.choice(options)
    playerInput = input("Rock, Paper, Scissors️: ")
    if playerInput not in options:
        print("Choose From Options")
    elif playerInput == "Rock" and computer == "Rock":
        print("Play Again")
    elif playerInput == "Rock" and computer == "Paper":
        print("Computer Wins! 1 point")
        computerPoints += 1
    elif playerInput == "Rock" and computer == "Scissors":
        print("Player Wins! 1 point")
        playerPoints += 1
    elif playerInput == "Paper" and computer == "Rock":
        print("Player Wins! 1 point")
        playerPoints += 1
    elif playerInput == "Paper" and computer == "Paper":
        print("Play Again")
    elif playerInput == "Paper" and computer == "Scissors":
        print("Computer Wins! 1 point")
        computerPoints += 1
    elif playerInput == "Scissors" and computer == "Rock":
        print("Computer Wins! 1 point")
        computerPoints += 1
    elif playerInput == "Scissors" and computer == "Paper":
        print("Player Wins! 1 point")
        playerPoints += 1
    elif playerInput == "Scissors" and computer == "Scissors":
        print("Play Again")

    if playerPoints >= 3:
        print("-------------Game Over----------------")
        print(f"Player Won 🥳 with {playerPoints} Points")
        isCorrect = False
    elif computerPoints >= 3:
        print("-------------Game Over----------------")
        print(f"Computer Won 😎 with {computerPoints} Points")
        isCorrect = False


