import random


class TicTacToeGame:
    def __init__(self):
        self.currentPlayer = "X"
        self.winningCombos: list[list[tuple[int, int]]] = []
        self.availableSpots: list[tuple[int, int]] = []
        self.xSpots: list[tuple[int, int]] = []
        self.oSpots: list[tuple[int, int]] = []
        self.gameOver = False
        self.tttBoard: dict[tuple[int, int], str] = {}

    def play(self):
        self.InitializeWinningCombos()

        print("\nTic Tac Toe vs Computer! You are Player X. You will be playing against the Computer - Player O")

        for i in range(3):
            for j in range(3):
                self.availableSpots.append((i, j))

        while not self.gameOver:
            while self.currentPlayer == "X":
                row = 0
                col = 0

                while row < 1 or row > 3:
                    try:
                        row = int(input("\nEnter row (1-3): "))
                        if row < 1 or row > 3:
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid input. Please try again.")

                while col < 1 or col > 3:
                    try:
                        col = int(input("\nEnter column (1-3): "))
                        if col < 1 or col > 3:
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid input. Please try again.")

                row -= 1
                col -= 1

                if self.tttBoard.get((row, col)) != "X" and self.tttBoard.get((row, col)) != "O":
                    self.PlaceAndDetermineWinner(row, col)
                else:
                    print(f"\nThe spot at Row = {row + 1} and Col = {col + 1} is already taken. Try again.")

            """Player O - Random generation"""
            if not self.gameOver:
                if self.availableSpots.__len__() == 0:
                    print("\nThe board is full, game over! Its a tie.")
                    break
                index = random.randint(1, self.availableSpots.__len__())
                spot = random.choice(self.availableSpots)
                """r, c = self.availableSpots[index]"""

                print("\nComputer's turn, please see Computer's move in the board below.")

                self.PlaceAndDetermineWinner(spot[0], spot[1])

        print("\nExiting Game.")

    def InitializeWinningCombos(self):
        diagonal: list[tuple[int, int]] = []
        diagonal2: list[tuple[int, int]] = []

        for i in range(3):
            col: list[tuple[int, int]] = []
            row: list[tuple[int, int]] = []

            diagonal.append((i, i))
            diagonal2.append((i, 2 - i))

            for j in range(3):
                row.append((i, j))
                col.append((j, i))

            self.winningCombos.append(row)
            self.winningCombos.append(col)

        self.winningCombos.append(diagonal)
        self.winningCombos.append(diagonal2)

    def PlaceAndDetermineWinner(self, row, col):
        self.tttBoard[(row, col)] = self.currentPlayer
        self.printBoard()
        self.availableSpots.remove((row, col))

        if self.currentPlayer == "X":
            self.xSpots.append((row, col))
            self.gameOver = self.CheckForWinner(self.xSpots)
        elif self.currentPlayer == "O":
            self.oSpots.append((row, col))
            self.gameOver = self.CheckForWinner(self.oSpots)

        if self.gameOver:
            print(f"\n{self.currentPlayer} is the winner.")

        if self.currentPlayer == "X":
            self.currentPlayer = "O"
        else:
            self.currentPlayer = "X"

    def printBoard(self):
        for row in range(3):
            for col in range(3):
                print(self.tttBoard.get((row, col), "_"), end=" ")
            print()

    def CheckForWinner(self, playerSpots):
        for combo in self.winningCombos:
            if all(spot in playerSpots for spot in combo):
                return True
        return False


def main():
    game = TicTacToeGame()
    game.play()


if __name__ == "__main__":
    main()

