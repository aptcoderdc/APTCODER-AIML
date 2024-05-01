import random

class QuantumRockPaperScissors:
    def __init__(self):
        self.choices = ['Rock', 'Paper', 'Scissors']
        self.results = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}

    def play(self):
        # Player's choice
        player_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
        if player_choice not in self.choices:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")
            return

        # Quantum computer's choice (randomly generated)
        quantum_choice = random.choice(self.choices)

        # Determine the winner based on quantum mechanics
        if player_choice == quantum_choice:
            print("It's a tie!")
        elif self.results[player_choice] == quantum_choice:
            print("You win!")
        else:
            print("You lose!")

# Create an instance of the game
game = QuantumRockPaperScissors()

# Play the game
game.play()
