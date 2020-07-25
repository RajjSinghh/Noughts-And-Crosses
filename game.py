from player import *


def CreateBoard():
    board = []
    for i in range(3):
        row = ["-" for j in range(3)]
        board.append(row)
    return board


def PrintBoard(board):
    print("\n")
    for i in range(3):
        current_row = ""
        for j in range(3):
            current_row += f"|{board[i][j]}|"
        print(current_row)
        if i != 2:
            print("_________")
    print("\n")

def CheckWin(board):
    winner = "-"
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

def Game():
    players = [RandomPlayer("x"), Player("o")]
    winner = "-"
    board = CreateBoard()
    turn = 0

    while turn < 9 and winner == "-":
        players[turn %2].MakeMove(board)
        PrintBoard(board)
        winner = CheckWin(board)
        turn += 1

    if turn == 9:
        print("It's a draw!")
    else:
        print(f"{winner} wins!")
    
if __name__ == "__main__":
    Game()
