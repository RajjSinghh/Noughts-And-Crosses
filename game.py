from player import Player


def CreateBoard():
    board = []
    for i in range(3):
        row = ["-" for j in range(3)]
        board.append(row)
    return board


if __name__ == "__main__":
    board = CreateBoard()
    players = [Player("x"), Player("o")]
    players[0].MakeMove(board)
    players[1].MakeMove(board)
    print(board)
