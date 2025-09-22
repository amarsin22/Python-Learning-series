import random

def game():
  print("you are playing the game")
  score = random.randint(1,62)
  #Fetch the hiscore
  with open("hiscore.txt") as f:
    hiscore = f.read()
  print(f"Your Score: {score}")
  if(score>hiscore or hiscore==""):
    