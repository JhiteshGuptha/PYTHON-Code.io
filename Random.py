# Random Numbers = Generate Random values

import random

# Random Whole Integer = random.randint(start, end)
#                      = Returns an integer within the range mentioned
#                      = end is also inclusive

numberInt = random.randint(1, 6)
print(numberInt)

# Random Floating Number = random.random()
#                        = Between 0 and 1
#                        = Range does not imply here

numberFloat = random.random()
print(numberFloat)

# Pick a random choice from a sequence = random.choice(variable)

options = ("rock", "paper", "scissors")

choice = random.choice(options)
print(choice)

# Shuffle = random.shuffle(variable)
#         = You cannot output the shuffle to a variable

cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

random.shuffle(cards)
print(cards)