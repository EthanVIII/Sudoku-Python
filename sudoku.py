def main() -> None:
    game = Sudoku()
    print(game)

class Sudoku:
    board = [0 for i in range(81)]
    
    def __str__(self):
        bffer: str = ""
        for i in range(0,len(self.board),9):
            bffer += str(self.board[i:i+9]) + "\n"
        return bffer
    
    def __read__(self, file: ):
        

if __name__ == "__main__":
    main()

