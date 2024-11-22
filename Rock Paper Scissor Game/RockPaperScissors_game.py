import random

point_user = 0
point_computer =0
while True:
    user_input = input("Enter your choice (rock, paper, scissors) ")
    possible_choices = ["rock", "paper", "scissors"]
    computer_input = random.choices(possible_choices)
    computer_input = random.choice(possible_choices)

    print("User choice: " + user_input)
    print("Computer choice: " +computer_input)

    if user_input == computer_input:
        print(f"Its a Draw as both selected {user_input}")
    elif user_input =="rock":
        if computer_input == "scissors":
            print("User wins, Rock will break the scissors")
            point_user +=1
        else:
            print("User loose, Paper will cover rock")
            point_computer +=1
    elif user_input =="paper":
        if computer_input == "rock":
            print("User wins, Paper will cover rock")
            point_user +=1
        else:
            print("User loose, Scissors will cut the paper")
            point_computer +=1
    elif user_input =="scissors":
        if computer_input == "paper":
            print("User wins, Scissors will cut the paper")
            point_user +=1
        else:
            print("User loose, Rock will break the scissors")
            point_computer +=1
    play_again = input("Do you want to play again? (y/n): ") # when User loose the game this command (play_again) will run
    if play_again.lower() != "y":
        break

print(f"Total Points are: User {point_user}  Computer: {point_computer}")        
print("Game Over")