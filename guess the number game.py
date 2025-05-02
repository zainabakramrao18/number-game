import random

def choose_difficulty():
    print("\n🎯 Choose a difficulty level:")
    print("1. Easy (1–50)")
    print("2. Medium (1–100)")
    print("3. Hard (1–200)")
    
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == '1':
            return 50
        elif choice == '2':
            return 100
        elif choice == '3':
            return 200
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")

def get_user_guess(max_range):
    while True:
        try:
            guess = int(input(f"👉 Your guess (1–{max_range}): "))
            if 1 <= guess <= max_range:
                return guess
            else:
                print(f"🚫 Guess must be between 1 and {max_range}!")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def play_game():
    max_number = choose_difficulty()
    number_to_guess = random.randint(1, max_number)
    attempts = 0
    print(f"\nI'm thinking of a number between 1 and {max_number}...")

    while True:
        guess = get_user_guess(max_number)
        attempts += 1

        if guess < number_to_guess:
            print("🔼 Too low! Try again.")
        elif guess > number_to_guess:
            print("🔽 Too high! Try again.")
        else:
            print(f"🎉 Correct! The number was {number_to_guess}.")
            print(f"🥳 You guessed it in {attempts} tries.\n")
            break

def guess_the_number():
    print("🎲 Welcome to Guess the Number!")
    while True:
        play_game()
        play_again = input("🔁 Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("👋 Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    guess_the_number()
