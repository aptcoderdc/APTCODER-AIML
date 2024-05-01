import numpy as np

class QuantumTicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3))  # Initialize empty 3x3 board
        self.current_player = 1  # Player 1 starts the game

    def make_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.current_player = -1 if self.current_player == 1 else 1  # Switch players
        else:
            print("Invalid move! Position already taken.")

    def check_winner(self):
        for player in [1, -1]:
            # Check rows and columns for a win
            if np.any(np.all(self.board == player, axis=0)) or np.any(np.all(self.board == player, axis=1)):
                return player
            # Check diagonals for a win
            if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
                return player
        # Check for a draw
        if np.all(self.board != 0):
            return 0
        # Game is still ongoing
        return None

    def display_board(self):
        symbols = {1: 'X', -1: 'O', 0: ' '}
        for row in self.board:
            print("|".join([symbols[val] for val in row]))
            print("-----")

# Example usage
game = QuantumTicTacToe()
game.display_board()
while True:
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    game.make_move(row, col)
    game.display_board()
    winner = game.check_winner()
    if winner is not None:
        if winner == 0:
            print("It's a draw!")
        else:
            print(f"Player {winner} wins!")
        break
