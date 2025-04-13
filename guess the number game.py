import random

def guess_the_number():
    print("🎲 Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100...")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("👉 Your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("🚫 Guess must be between 1 and 100!")
            elif guess < number_to_guess:
                print("🔼 Too low! Try again.")
            elif guess > number_to_guess:
                print("🔽 Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {number_to_guess}.")
                print(f"🥳 You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
