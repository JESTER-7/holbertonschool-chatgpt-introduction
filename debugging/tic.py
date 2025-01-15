#!/usr/bin/python3
def print_board(board):
    """
    Print the current state of the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check for a winner on the Tic Tac Toe board.
    Returns True if there's a winner, otherwise False.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Main function to run the Tic Tac Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves_count = 0

    while moves_count < 9:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == " ":
                board[row][col] = player
                moves_count += 1
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    break
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        else:
            print("Invalid row or column. Please enter values between 0 and 2.")

    # Check for draw after all moves are made and no winner
    if moves_count == 9:
        print_board(board)
        print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()