def CreateBoard():
    board = []
    for i in range(3):
        row = [0 for j in range(3)]
        board.append(row)
    return board


if __name__ == "__main__":
    board = CreateBoard()
    players = [Player(x), Player(y)]
    print(board)
