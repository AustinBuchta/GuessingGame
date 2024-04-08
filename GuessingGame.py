
import random

def display_the_heading():
    print("Welcome to the Number Guessing Game!")
    print("-----------------------------------")

def play_game(limit):
    secret_number = random.randint(1, limit)
    print(f"I'm thinking of a number between 1 and {limit}. Can you guess what it is?")
    while True:
        user_guess = int(input("Enter your guess: "))
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            break
    play_again = input("Do you want to play again? (y/n): ").lower()
    return play_again == 'y'

def main():
    display_the_heading()
    while True:
        limit = int(input("Enter the limit: "))
        play_again = play_game(limit)
        if not play_again:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()