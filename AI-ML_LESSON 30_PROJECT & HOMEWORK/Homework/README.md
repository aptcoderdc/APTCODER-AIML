# Guess the Number Game with Hyperparameter Tuning


Welcome to the Guess the Number Game with Hyperparameter Tuning! This project introduces the concept of hyperparameters through a simple and interactive guessing game.


## Objective
The objective of this project is to introduce kids to the concept of hyperparameters in a fun and engaging way by allowing them to play a "Guess the Number" game where they can adjust the maximum number of attempts to find the optimal difficulty level.


## How to Play
1. Run the Python script `guess_the_number.py`.
2. The computer will randomly select a number between 1 and 100.
3. You have a certain number of attempts to guess the secret number.
4. After each guess, you'll receive feedback if your guess is too high or too low.
5. Keep guessing until you find the secret number or run out of attempts.


## Hyperparameter Tuning
You can adjust the maximum number of attempts to make the game easier or harder. Experiment with different values to find the optimal difficulty level.


## Getting Started
To get started with the game, make sure you have Python installed on your system. You can run the game by executing the `guess_the_number.py` script in your preferred Python environment.


## Example
Here's an example of playing the game with default and tuned maximum attempts:


```python
# Play the game with default maximum attempts
guess_the_number()


# Tune the maximum number of attempts
tuned_max_attempts = 5
print(f"\nPlaying the game with {tuned_max_attempts} maximum attempts:")
guess_the_number(max_attempts=tuned_max_attempts)
