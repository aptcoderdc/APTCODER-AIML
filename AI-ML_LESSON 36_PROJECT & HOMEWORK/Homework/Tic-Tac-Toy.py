import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for row in board:
        if all(mark == player for mark in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def make_ai_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    return random.choice(empty_cells)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        if player == "X":
            row, col = map(int, input("Enter row and column (0-2) to place 'X': ").split())
        else:
            row, col = make_ai_move(board)
            print(f"AI placed 'O' at row {row}, column {col}")

        if board[row][col] == " ":
            board[row][col] = player
            print_board(board)

            if check_win(board, player):
                print(f"Player {player} wins!")
                break
            elif check_draw(board):
                print("It's a draw!")
                break
            else:
                turn += 1
        else:
            print("That cell is already occupied. Try again.")

if __name__ == "__main__":
    main()
