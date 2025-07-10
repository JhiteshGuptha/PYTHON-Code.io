import random

# ● ┌ ─ ┐ │ └ ┘

diceArt = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
        ),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"
        ),
    3: ("┌─────────┐",
        "│    ●    │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
        ),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
        ),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
        ),
    6: ("┌─────────┐",
        "│ ●  ●  ● │",
        "│         │",
        "│ ●  ●  ● │",
        "└─────────┘"
        ),
}

total = 0
dice = []
diceNumber = int(input("How many Dice you wanna roll?: "))

for i in range(diceNumber):
    dice.append(random.randint(1, 6))

for line in range(5):
    for x in dice:
        print(diceArt.get(x)[line], end="")
    print()

for j in dice:
    total = total + j

print(f"Total of Dice Rolls: {total}")

