import random

def Play_game():
    """Plays a game of Rock, Paper, Scissors."""

    # User Input
    User_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Computer Selection
    comp_choice = random.choice(["rock", "paper", "scissors"])

    # Game Logic
    if User_choice == comp_choice:
        result = "It's a tie!"
    elif (User_choice == "rock" and comp_choice == "scissors") or \
         (User_choice == "paper" and comp_choice == "rock") or \
         (User_choice == "scissors" and comp_choice == "paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    # Display Result
    print(f"\nYou chose: {User_choice}")
    print(f"Computer chose: {comp_choice}")
    print(f"\n{result}")

# Play the game
Play_game()
