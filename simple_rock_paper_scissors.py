import random


def get_choices():
    player_choice = input("Enter a choice (rock,paper,scissors:)\n")
    comp = ["rock", "paper", "scissors"]
    computer_choice = random.choice(comp)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player}.\nComputer chose {computer}.")
    if player == computer:
        return ("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            return ("Rock smashes scissors. You win!")
        else:
            return ("Paper covers rock. You lose..")
        exit(0)
    elif player == "scissors":
        if computer == "rock":
            return ("Rock smashes scissors. You lose..")
        else:
            return ("Scissors cut paper. You win!")
        exit(0)
    else:
        if computer == "rock":
            return ("Paper covers rock. You win!")
        else:
            return ("Scissors cut paper. You lose..")
        exit(0)


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
