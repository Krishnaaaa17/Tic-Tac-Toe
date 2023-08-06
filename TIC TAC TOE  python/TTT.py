def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Check columns
            return True
    if all(board[i][i] == player for i in range(3)):  # Check main diagonal
        return True
    if all(board[i][2-i] == player for i in range(3)):  # Check anti-diagonal
        return True
    return False
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True
def tic_tac_toe():
    board = initialize_board()
    players = ["X", "O"]
    turn = 0

    while True:
        display_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        # Get the player's move (row and column)
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        # Check if the chosen position is empty
        if board[row][col] == " ":
            board[row][col] = player

            # Check if the current player wins
            if check_winner(board, player):
                display_board(board)
                print(f"Player {player} wins!")
                break

            # Check if it's a draw
            if check_draw(board):
                display_board(board)
                print("It's a draw!")
                break

            turn += 1
        else:
            print("That position is already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
