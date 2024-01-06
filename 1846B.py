t = int(input())


def check_winner(board):
    # check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != ".":
            return row[0]

    # check columns
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != ".":
            return board[0][col]

    # check diagonals
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != ".":
        return board[0][0]
    if len(set([board[i][2-i] for i in range(3)])) == 1 and board[0][2] != ".":
        return board[0][2]

    # no winner
    return None


for _ in range(t):
    board = [list(input()), list(input()), list(input())]

    if winner := check_winner(board):
        print(winner)
    else:
        print("DRAW")
