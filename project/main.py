# 1 for snake
# -1 for water
# 0 for gun

import random

# Computer's choice (randomly)
computer = random.choice([1, -1, 0])

# User input
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Convert user choice
you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

# Game logic
if computer == you:
    print("It's a Draw!")

elif (computer == -1 and you == 1):  # Snake drinks Water
    print("You Win!")

elif (computer == 1 and you == 0):  # Gun kills Snake
    print("You Win!")

elif (computer == 0 and you == -1):  # Water disables Gun
    print("You Win!")

else:
    print("You Lose!")
