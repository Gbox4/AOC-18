serialNumber=5719

def getHundreds(number):
    if number < 100:
        return(0)
    else:
        return(int(str(number)[len(str(number))-3]))

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

for y in range(1,301):
    newLine = []
    for x in range(1,301):
        newLine.append(Point(x,y))
    board.append(newLine)

highestSquare = Point(0,0)
highestPower = 0

for y in range(len(board)):
    for x in range(len(board[y])):
        if x > 296 or y > 296:
            break

        squarePower = 0
        for sy in range(y,y+3):
            for sx in range(x,x+3):
                squarePower += board[sy][sx].powerLevel
        
        if squarePower > highestPower:
            highestPower = squarePower
            highestSquare = board[y][x]


print("Program end.")