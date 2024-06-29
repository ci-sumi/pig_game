import random

def dice():
    min_dice=1
    max_dice=6
    randomN = random.randint(min_dice,max_dice)
    return randomN

while True:
    current_score=0
    players= input("Enter number of players(1-4?:")
    if players.isdigit():
        players = int(players)
        if 1<=players <=4:
            break
        else:
            print("Players must between(1-4)")
    else:
        print("Enter a valid number")

max_score = 50
players_score =[0 for _ in range(players)]
print(players_score)
while max(players_score) < max_score:
    for players_index in range (players):
        while True:
            print(f"Player {players_index+1}'s turn has started")
            should_dice =input("Do u want to dice y/n?:")
            if should_dice.lower()!="y":
                break
            value = dice()
            if value==1:
                print("You rolled 1! You turn over")
                current_score =0
                break
            else:
                current_score+=value
                print(f"You rolled a {value} and your current turn score is {current_score}")
                
        players_score[players_index]+=current_score
        print("Your total score is",players_score[players_index])
        
max_score =max(players_score)
winning_index =players_score.index(max_score)
print(f"Player {winning_index + 1} wins with a score of {max_score}!")



    
        