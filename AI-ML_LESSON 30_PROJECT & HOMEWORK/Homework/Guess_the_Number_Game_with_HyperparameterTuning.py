import random


def guess_the_number(max_attempts=10):
    print("Welcome to Guess the Number Game!")
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while attempts < max_attempts:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            return
        
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")


# Play the game with default maximum attempts
guess_the_number()


# Tune the maximum number of attempts
tuned_max_attempts = 5
print(f"\nPlaying the game with {tuned_max_attempts} maximum attempts:")
guess_the_number(max_attempts=tuned_max_attempts)
