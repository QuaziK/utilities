import random

SIDE_LENGTH = 3
NUM_MINES = 2
available = list(range(SIDE_LENGTH**2))
mines = []

class Coord:
    def __init__(self, i, j=None):
        if j is not None:            
            self.i = i
            self.j = j
            self.num = i*SIDE_LENGTH+j
        else:
            self.i = i//SIDE_LENGTH
            self.j = i%SIDE_LENGTH
            self.num = i
    
    def __eq__(self, other):
        if self.i == other.i and self.j == other.j and self.num == other.num:
            return True
        else:
            return False
    
    def __str__(self):
        return f"(i:{self.i}, j: {self.j}, num:{self.num})"
    
    def __repr__(self):
        return str(self)
        
def getSurroundingCoords(coord):
    i = coord.i
    j = coord.j
    allSurround = [[i-1,j-1], [i-1,j], [i-1,j+1], [i,j-1], [i,j+1], [i+1,j-1], [i+1,j], [i+1,j+1]]
    surround = []
    for i,j in allSurround:
        if i < SIDE_LENGTH and i >= 0 and j < SIDE_LENGTH and j >= 0 and Coord(i*SIDE_LENGTH+j) not in mines:
            surround.append(Coord(i=i,j=j))
            
    return surround

def placeMines(mines):
    board = [[0 for j in range(SIDE_LENGTH)] for i in range(SIDE_LENGTH)]
    for mine in mines:
        i = mine.i
        j = mine.j
        board[i][j] = 'X'
        surround = getSurroundingCoords(mine)
        for coord in surround:
            print(mine, coord.i, coord.j)
            i = coord.i
            j = coord.j
            board[i][j] = int(board[i][j]) + 1
    
    return board
  
def printBoard(board):
    for i in board:
        for j in i:
            print(str(j)+' ', end='')
        print('\n')

for i in range(NUM_MINES):
    select = random.choice(available)
    available.remove(select)
    mines = mines + [Coord(i=select)]
    # mines = [Coord(i=1,j=0)]

print(mines)
board = placeMines(mines)
printBoard(board)



