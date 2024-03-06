from art import logo 
from art import vs 
from game_data import data
import random
import os

def GeneratePlayer():
  RandomAccount = random.choice(data)
  return RandomAccount

def CheckWinner(A, B):
  if A > B:
    return "A"
  elif B > A: 
    return "B"
  else: return "D"

def game():  
  PlayerLost = False
  PlayerScore = 0
  RandomA = GeneratePlayer()
  RandomB = GeneratePlayer()
  while not PlayerLost:
    os.system('clear')
    print(f"hmmmm A:{RandomA['follower_count']}, B:{RandomB['follower_count']}")
    Winner = CheckWinner(RandomA['follower_count'], RandomB['follower_count'])
    print(logo)
    print(f"Compare A: {RandomA['name']}, a {RandomA['description']}, from {RandomA['country']}.")
    print(vs)
    print(f"Against B: {RandomB['name']}, a {RandomB['description']}, from {RandomB['country']}.")
    Answer = input("Who has more followers? Type 'A' or 'B':")
    if Answer == Winner or Winner == "D":
      PlayerScore += 1
      print(f"Good Job! Your score is now : {PlayerScore}")
      RandomA = RandomB
      RandomB = GeneratePlayer()
    else: 
      os.system('clear')
      print(logo)
      print(f"Sorry, that's wrong. Final score: {PlayerScore}")
      PlayerLost = True
game()  