# We will write a rock paper scissors game in class - Complete it in this file
import random
player_choice="rock"
computer_choice="paper"
def get_choices():
    options=["rock","paper","scissors"]
    player_choice=input("Enter choice:")
    computer_choice=random.choice(options)
    choices={"player": player_choice, "computer": computer_choice}
    return choices

choices=get_choices()
print(choices)
if choices["player"]==choices["computer"]:
    print("tie")
elif ((choices["player"]=="rock" and choices["computer"]=="scissors") or (choices["player"]=="paper" and choices["computer"]=="rock") or (choices["player"]=="scissors" and choices["computer"]=="paper")):
    print("player wins")
else:
    print("computer wins")

