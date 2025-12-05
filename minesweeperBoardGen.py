import random

SIDE_LENGTH = 10
NUM_MINES = 10
available = list(range(SIDE_LENGTH**2))
mines = []

class Coord:
    i = 0
    j = 0
    num = 0
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.num = convertCoords(i,j)
    
    def __init__(self, num):
        self.i, self.j = convertCoords(num)
        self.num = num
        
    def convertCoords(*args, **kwargs):
        if len(args)==1:
            return [int(args[0])/SIDE_LENGTH, int(args[0])%SIDE_LENGTH]
        elif len(args)==2:
            return int(args[0])*SIDE_LENGTH+int(args[1])
        else:
            return None
    

def getSurroundingCoords(num):
    i = int(num/SIDE_LENGTH)
    j = int(num%SIDE_LENGTH)
    allSurround = [[i-1,j-1], [i-1,j], [i-1,j+1], 
                   [i,j-1],            [i,j+1], 
                   [i+1,j-1], [i+1,j], [i+1,j+1]]
    surround = []
    for i,j in allSurround:
        if i < SIDE_LENGTH and i >= 0 and j < SIDE_LENGTH and j >= 0 and i*SIDE_LENGTH+j not in mines:
            surround.append([i,j])
            
    return surround

def placeMines(mines):
    board = [['0' for j in range(SIDE_LENGTH)] for i in range(SIDE_LENGTH)]
    for mine in mines:
        i = int(mine/SIDE_LENGTH)
        j = int(mine%SIDE_LENGTH)
        board[i][j] = 'X'
        surround = getSurroundingCoords(mine)
        for i,j in surround:
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
    mines = mines + [select]

board = placeMines(mines)
printBoard(board)



