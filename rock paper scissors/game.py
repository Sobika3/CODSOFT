import random

choices = ("rock", "paper", "scissors")
playing = True

while playing:
    user_choice = None
    computer_choice = random.choice(choices)

    while user_choice not in choices:
        user_choice = input("Enter your choice (rock, paper, scissors): ")

    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

    if not input("Do you want to play again? (y/n): ").lower() == "y":
        playing = False

print("Thanks for playing!")
