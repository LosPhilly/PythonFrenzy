board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

def player_input(player):
    row = int(input("Enter row (0, 1, 2): "))
    col = int(input("Enter col (0, 1, 2): "))
    if board[row][col] == ' ':
        board[row][col] = player
    else:
        print("Space already filled. Try again.")
        player_input(player)

def check_win():
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != ' ':
            return board[row][0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != ' ':
        return board[2][0]
    return None

def check_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True


def tic_tac_toe():
    while True:
        player_input("X")
        winner = check_win()
        if winner:
            print(f"Player {winner} wins!")
            break
        if check_full():
            print("Tie!")
            break
        player_input("O")
        winner = check_win()
        if winner:
            print(f"Player {winner} wins!")
            break
        if check_full():
            print("Tie!")
            break

tic_tac_toe()

