Quantum-inspired Tic-Tac-Toe Game

## Overview
This project implements a quantum-inspired version of the classic Tic-Tac-Toe game. Players take turns placing their symbols ('X' or 'O') on a 3x3 board, and the game continues until one player wins or the board is full, resulting in a draw. The game logic is based on classical rules, but the concept is inspired by quantum principles.

## Concepts Covered
Object-oriented programming in Python
Numpy for array manipulation
Conditional statements
Loops
User input
Printing formatted output

## Required Libraries
Numpy

## Setup
Ensure you have Python installed on your system. If not, download and install it from python.org.
Install the required library using pip:

pip install numpy

Download the QuantumTicTacToe.py file to your local machine.

## How to Run
Open a terminal or command prompt.
Navigate to the directory containing the QuantumTicTacToe.py file.
Run the script using the following command:

python QuantumTicTacToe.py

## Usage
The game will display an empty Tic-Tac-Toe board.
Enter the row and column where you want to place your symbol ('X' or 'O').
The game will alternate between players until one wins or the board is full.
If a player wins, the game will display the winning message. If the board is full without a winner, it will declare a draw.
You can choose to play again or exit the game.

## Example

| | | |
-----
| | | |
-----
| | | |
-----
Enter row (0-2): 1
Enter column (0-2): 1
| | | |
-----
| |X| |
-----
| | | |
-----
Enter row (0-2): 0
Enter column (0-2): 0
|O| | |
-----
| |X| |
-----
| | | |
-----
...