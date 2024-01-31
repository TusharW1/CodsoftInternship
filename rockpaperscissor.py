import random

def play_round():
    choices = ["rock", "paper", "scissors"]

    # User input and validation
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Computer selection
    computer_choice = random.choice(choices)

    # Display choices
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!", 1, 0
    else:
        return "You lose!", 0, 1

def main():
    user_score = 0
    computer_score = 0

    while True:
        result, user_round_score, computer_round_score = play_round()
        user_score += user_round_score
        computer_score += computer_round_score

        print(result)
        print(f"Your score: {user_score}  Computer's score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
