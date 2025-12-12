import random

SIDE_LENGTH = 10
NUM_MINES = 10
available = list(range(SIDE_LENGTH**2))
mines = []

class Board:
    def __init__(self, side_length, num_mines):
        self.SIDE_LENGTH = side_length
        self.NUM_MINES = num_mines
        self.board = [[Coord(arg1=i,val='0',arg2=j) for j in range(self.SIDE_LENGTH)] for i in range(self.SIDE_LENGTH)]
        available = list(range(self.SIDE_LENGTH**2))
        self.mines = []
        for i in range(self.NUM_MINES):
            select = random.choice(available)
            available.remove(select)
            self.mines = self.mines + [Coord(arg1=select,val='X',arg2=None)]

class Coord:
    def __init__(self, arg1,val='0', arg2=None):
        if arg2 is not None:            
            self.i = arg1
            self.j = arg2
            self.num = arg1*SIDE_LENGTH+arg2
            self.val = val
        else:
            self.i = arg1//SIDE_LENGTH
            self.j = arg1%SIDE_LENGTH
            self.num = arg1
            self.val = val
        
        if val is not None:
            self.val = val
        else:
            self.val = '0'
    
    def __eq__(self, other):
        if self.i == other.i and self.j == other.j and self.num == other.num and self.val == other.val:
            return True
        else:
            return False
    
    def __str__(self):
        return f"(i:{self.i}, j: {self.j}, num:{self.num})"
    
    def __repr__(self):
        return str(self)

#get all surrounding Coord of the passed coordinate, excluding all those that fall beyon the board limits
#input: coord(Coord object that which yo uwant to find surrounding Coords), board(Board object in which coords are)
#output: list of Coord        
def getSurroundingCoords(coord,board):
    i = coord.i
    j = coord.j
    
    allSurround = [[i-1,j-1], [i-1,j], [i-1,j+1], [i,j-1], [i,j+1], [i+1,j-1], [i+1,j], [i+1,j+1]]
    returnSurround = []
    
    for i,j in allSurround:
        if i < SIDE_LENGTH and i >= 0 and j < SIDE_LENGTH and j >= 0:
            returnSurround.append(board[i][j])
            
    return returnSurround

#return a board with mines placed and correct hint numbers
#input: mines(1d list of Coords)
#output: board(2d list of Coords)
def placeMines(mines):
    board = [[Coord(arg1=i,val='0',arg2=j) for j in range(SIDE_LENGTH)] for i in range(SIDE_LENGTH)]
    for mine in mines:
        i = mine.i
        j = mine.j
        board[i][j].val = 'X'
        for coord in getSurroundingCoords(mine,board):
            coordMine = Coord(arg1=coord.num, val='X')
            if coordMine not in mines:
                i = coord.i
                j = coord.j
                board[i][j].val = str(int(board[i][j].val) + 1)

    
    return board

#print val of all Coords in board with easy to read spacing
#input: board(2d list of Coord)  
def printBoard(board):
    for i in board:
        for j in i:
            print(j.val+' ', end='')
        print('\n')

#check if board has correct hint numbers according to the number of mines
#input: board(2d list of Coords)
def checkBoard(board):
    for row in board:
        for coord in row:
            surround = getSurroundingCoords(coord,board)
            if coord.val == 'X':
                if '0' in [crd.val for crd in surround]:
                    return False 
            else:
                if int(coord.val) != [crd.val for crd in surround].count('X'):
                    return False 
    return True

for i in range(NUM_MINES):
    select = random.choice(available)
    available.remove(select)
    mines = mines + [Coord(arg1=select,val='X',arg2=None)]

board = placeMines(mines)
printBoard(board)
print(checkBoard(board))



