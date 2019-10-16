serialNumber=5719
gridSize=300

def getHundreds(number):
    if number < 100:
        return(0)
    else:
        return(int(str(number)[len(str(number))-3]))

def printBoard(board):
    for y in board:
        line = ""
        for x in y:
            if x.powerLevel < 0:
                line = line + "  " + str(x.powerLevel) 
            else:
                line = line + "   " + str(x.powerLevel)
        print(line)

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

        self.rackID=self.x+10

        self.powerLevel=self.rackID*self.y
        self.powerLevel+=serialNumber
        self.powerLevel=self.powerLevel*self.rackID
        self.powerLevel=getHundreds(self.powerLevel)
        self.powerLevel-=5


board = []

for y in range(1,gridSize+1):
    newLine = []
    for x in range(1,gridSize+1):
        newLine.append(Point(x,y))
    board.append(newLine)


highestSquare = Point(0,0)
highestPower = 0
highestSize = 0

for y in range(len(board)):
    for x in range(len(board[y])):
        squarePower = 0
        
        for size in range(1,min(gridSize-y,gridSize-x)):
            newRowIndex=y+size-1
            newColIndex=x+size-1
            for p in range(x,x+size):
                squarePower+=board[newRowIndex][p].powerLevel
            if size <= 1:
                continue
            for p in range(y,y+size-1):
                squarePower+=board[p][newColIndex].powerLevel
                

            if squarePower > highestPower:
                highestPower = squarePower
                highestSquare = board[y][x]
                highestSize = size
            



print (highestPower,highestSize)
print (highestSquare.x,highestSquare.y)