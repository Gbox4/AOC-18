class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = 0
        self.disqualified = False
        self.territory = []
        self.closest = None
        self.totaldist = 0
        self.lessthan10000 = False
    
    def printInfo(self):
        print("x:",self.x,"\ny:",self.y,"\narea:",self.area)
    
    def calcArea(self):
        self.area = len(self.territory)
    

    def calcTotalDist(self,coords):
        for i in coords:
            self.totaldist += distanceBetween(i, self)
        
        if self.totaldist < 10000:
            self.lessthan10000 = True
            return True
        
        else:
            return False

test = """
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
"""

puzzle = """
315, 342
59, 106
44, 207
52, 81
139, 207
93, 135
152, 187
271, 47
223, 342
50, 255
332, 68
322, 64
250, 72
165, 209
129, 350
139, 118
282, 129
311, 264
216, 246
134, 42
66, 151
263, 199
222, 169
236, 212
320, 178
202, 288
273, 190
83, 153
88, 156
284, 305
131, 90
152, 88
358, 346
272, 248
317, 122
166, 179
301, 307
156, 128
261, 290
268, 312
89, 53
324, 173
353, 177
91, 69
303, 164
40, 221
146, 344
61, 314
319, 224
98, 143
"""

def parse(instr):
    coords = []
    x = ""
    y = ""
    for i in range(len(instr)):
        if instr[i] == "\n":
            for j in range(i+1,len(instr)):
                if instr[j] == ",":
                    break
                else:
                    x = x + instr[j]
        
        if instr[i] == ",":
            for j in range(i+2,len(instr)):
                if instr[j] == "\n":
                    coords.append(Point(int(x),int(y)))
                    x = ""
                    y = ""
                    break
                else:
                    y = y + instr[j]



    return coords

def distanceBetween(point1,point2):
    dis = abs(point1.x - point2.x) + abs(point1.y - point2.y)
    return dis

def isOnEdge(point, xmax, xmin, ymax, ymin):
    xmax -= 2
    ymax -= 2
        
    if point.x == xmax or point.x == xmin or point.y == ymax or point.y == ymin:
        return True
    
    else:
        return False

coords = parse(puzzle)

xmax = 0
xmin = 0
ymax = 0
ymin = 0



for i in coords:
    if i.x > xmax:
        xmax = i.x
    if i.y > ymax:
        ymax = i.y

xmax += 2
xmin = 0
ymax += 2
ymin = 0

board = []

for i in range(ymin,ymax):
    newRow = []
    for j in range(xmin,xmax):
        newPoint = Point(j,i)
        #if j == xmax or j == xmin or i == ymax or i == ymin:
            #newPoint.disqualified = True
        newRow.append(newPoint)
        
    board.append(newRow)


reigonArea = 0

for y in board:
    for p in y:
        if p.calcTotalDist(coords):
            reigonArea += 1

print(reigonArea)




#answer: x-250 y-72 area-4290