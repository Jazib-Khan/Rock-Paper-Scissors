from random import randint

# create a list of options
t = ["Rock", "Paper", "Scissors"]

# assign a random player to the computer
computer = t[randint(0,2)]

# set player to false
player = False

while player == False:
    #set player to True
    player = input("Rock, Paper, Scissors? ").lower()
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", player)
    elif player == "paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!,", player, "covers", computer)
    elif player == "scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)
    else:
        print("That's not a valid play, check your spelling")

    # player was set to True, but we want it to be False to keep the loop going
    player = False
    computer = t[randint(0,2)]
