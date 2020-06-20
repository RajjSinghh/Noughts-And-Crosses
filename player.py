class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def MakeMove(self, board):
        print(f"{self.symbol}'s turn")
        acceptable = False
        while not acceptable:
            try:
                row = int(input("Enter the row: "))
                column = int(input("Enter Column: "))
                if row < 0 or row > 2 or column < 0 or column > 2:
                    print("Not valid board position")
                    raise ValueError("Not valid board position")
                elif board[row][column] != "-":
                    print("Square already taken")
                    raise ValueError("Square already taken")
                else:
                    acceptable = True
            except:
                pass
        board[row][column] = self.symbol
