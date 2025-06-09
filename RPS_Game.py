import random

options = ("Rock" , "Paper", "Scissors")

player = None
comp_score = 0
player_score = 0

while True:
    comp = random.choice(options)
    player = input("Enter your choice from Rock, Paper or Scissors or q to quit: ")

    if player == 'q':
        break
    elif comp == player:
        print("Draw!")
    elif (comp == "Scissors" and player == "Paper") or (comp == "Rock" and player == "Scissors") or (comp == "Paper" and player == "Rock"):
        print("Computer wins this round!")
        comp_score += 1
    elif (player == "Scissors" and comp == "Paper") or (player == "Rock" and comp == "Scissors") or (player == "Paper" and comp == "Rock"):
        print("Player wins this round!")
        player_score += 1


if player_score > comp_score:
        print(f"Player Wins with {player_score} points!")
elif comp_score > player_score:
        print(f"Computer Wins with {comp_score} points!")
else:
        print(f"Draw with {comp_score} for each!")