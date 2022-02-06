import sys
import time
def main() -> None:
    name = sys.argv[1]
    game = Sudoku()
    for i in range(50):
        game.board = game.read(name,i)
        print("Problem:")
        print("-"*27)
        print(game)    
        tic = time.perf_counter()
        game.board = brute_force(game.board,0,0)
        toc = time.perf_counter()
        print("Solution:")
        print("-"*27)
        print(game)
        print(f"Solved in {toc-tic:0.4f} seconds")

def index(x: int, y: int) -> int:
    return x + 9*y

class Sudoku:
    board = []
    
    def __init__(self):
        self.board = [0 for i in range(81)]
    
    def __str__(self):
        bffer: str = ""
        for i in range(0,len(self.board),9):
            bffer += str(self.board[i:i+9]) + "\n"
        return bffer

    def read(self, file_name: str, count: int ):
        board = [0 for i in range(81)]
        with open(file_name) as file:
            lines = file.readlines()
            x,y = 0,0
            for i in lines[(10*count)+1:(10*count)+1+9]:
                for j in i:
                    if j != '\n':
                        board[index(x,y)] = int(j)
                    x += 1
                x = 0
                y += 1
        return board

def brute_force(board: list[int],x:int,y:int) -> list[int]:
    (valid,complete) = check_valid(board)
    if not valid:
        return None
    if complete and valid:
        return board
    if board[index(x,y)] == 0:
        if x == 8:
            if y == 8:
                x_next,y_next = 0,0
            else:
                x_next, y_next = 0, y+1
        else:
            x_next, y_next = x+1,y
        list_moves = []
        for i in range(1,10):
            c_board = board.copy()
            c_board[index(x,y)] = i
            temp_calc = brute_force(c_board,x_next,y_next) 
            if temp_calc != None:
                (valid_temp, complete_temp) = check_valid(temp_calc)
                if valid_temp and complete_temp:
                    return temp_calc
        return None
                
    else:
        if x == 8:
            if y == 8:
                print("Note: ended index search, x=8 & y=8")
                return None
            x_next, y_next = 0, y+1
        else:
            x_next, y_next = x+1,y

        return brute_force(board,x_next,y_next)

    print("Note: went to end of function")
    return None


def check_valid(board: list[int]) -> (bool,bool):
    complete_flag = True
    for i in range(0,81,9):
        build_check = set()
        subset = board[i:i+9]
        if len(set(subset)) != 9:
            complete_flag = False
        for o in subset:
            if o == 0:
                complete_flag = False
            if (o in build_check):
                if o != 0:
                    return (False, None)
            else:
                build_check.add(o)
    for i in range(0,9):
        build_check = set()
        subset = board[i::9]
        if len(set(subset)) != 9:
            complete_flag = False
        for o in subset:
            if o == 0:
                complete_flag = False
            if (o in build_check):
                if o != 0:
                    return (False, None)
            else:
                build_check.add(o)

    for i in range(0,9,3):
        for j in range(0,9,3):
            start = index(i,j)
            subset = board[index(i,j):index(i+3,j)]
            subset += board[index(i,j+1):index(i+3,j+1)]
            subset += board[index(i,j+2):index(i+3,j+2)]
            build_check = set()
            if len(set(subset)) != 9:
                complete_flag = False
            for o in subset:
                if o == 0:
                    complete_flag = False
                if (o in build_check):
                    if o != 0:
                        return (False, None)
                else:
                    build_check.add(o)``
    return (True,complete_flag)


if __name__ == "__main__":
    main()

