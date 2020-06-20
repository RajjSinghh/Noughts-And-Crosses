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


if __name__ == "__main__":
    board = CreateBoard()
    players = [Player("x"), Player("o")]
    players[0].MakeMove(board)
    players[1].MakeMove(board)
    PrintBoard(board)
