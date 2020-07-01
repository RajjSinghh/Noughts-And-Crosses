from player import Player


def CreateBoard():
    board = []
    for i in range(3):
        row = ["-" for j in range(3)]
        board.append(row)
    return board


def PrintBoard(board):
    for i in range(3):
        current_row = ""
        for j in range(3):
            current_row += f"|{board[i][j]}|"
        print(current_row)
        if i != 2:
            print("_________")

def CheckWin(board):
    winner = None
    for row in board:
        if row[0] == row[1] == row[2]:
            winner = row[0]
            break

    for column in range(3):
        if board[0][column] ==  board[1][column] == board[2][column]:
            winner = board[0][column]
            break

    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]

    return winner

if __name__ == "__main__":
#    board = CreateBoard()
#    players = [Player("x"), Player("o")]
#    players[0].MakeMove(board)
#    players[1].MakeMove(board)
#    PrintBoard(board)
    board = [["x", "x", "x"], ["o", "o", "-"], ["-", "-",  "-",]]
    PrintBoard(board)
    print(CheckWin(board))
    print("---------------------")
    
    board = [["x", "-", "-"], ["x", "-", "-"], ["x", "-",  "-",]]
    PrintBoard(board)
    print(CheckWin(board))
    print("---------------------")

    board = [["x", "-", "o"], ["x", "o", "-"], ["o", "-",  "x",]]
    PrintBoard(board)
    print(CheckWin(board))
    print("---------------------")

    board = [["x", "-", "o"], ["x", "x", "-"], ["o", "-",  "x",]]
    PrintBoard(board)
    print(CheckWin(board))
    print("---------------------")
