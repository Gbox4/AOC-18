from time import sleep

class Cart:
    def __init__(self,direction,x,y):
        #   Direction is found by x%4
        #   0 = up
        #   1 = right
        #   2 = down
        #   3 = left
        self.direction=direction
        self.turn=0
        self.x=x
        self.y=y
    
    def intersection(self):
        if self.turn%3==0:
            self.turnLeft()
        if self.turn%3==2:
            self.turnRight()
        
        self.turn+=1

    def turnLeft(self):
        self.direction-=1
    
    def turnRight(self):
        self.direction+=1
    
    def getDir(self):
        dirTranslation = ["up","right","down","left"]
        return(dirTranslation[self.direction%4])

def parse(filename):
    #Read the file and store in a list called rails
    f=open(filename,"r")
    rails=f.readlines()
    for i in range(len(rails)-1):
        rails[i] = rails[i][:-1]

    #Iterate through rails and at every cart, make a new cart in carts, and replace with - or | 
    carts=[]
    for y in range(len(rails)):
        for x in range(len(rails[y])):
            if rails[y][x]=="^":
                rails[y]=rails[y][:x]+"|"+rails[y][x+1:]
                carts.append(Cart(0,x,y))
            if rails[y][x]==">":
                rails[y]=rails[y][:x]+"-"+rails[y][x+1:]
                carts.append(Cart(1,x,y))
            if rails[y][x]=="v":
                rails[y]=rails[y][:x]+"|"+rails[y][x+1:]
                carts.append(Cart(2,x,y))
            if rails[y][x]=="<":
                rails[y]=rails[y][:x]+"-"+rails[y][x+1:]
                carts.append(Cart(3,x,y))
            
            rails[y] = rails[y]+" "
                


    return([rails,carts])

output = parse("day13input.txt")
rails = output[0]
carts = output[1]

ticks=0



running = True
while running:
    for c in carts:

        if c.direction==0:
            nextrail = rails[c.y-1][c.x]
            if nextrail == "|":
                c.y -= 1
            if nextrail == "/":
                c.y -= 1
                c.direction = 1
            if nextrail == "\\":
                c.y -= 1
                c.direction = 3
            if nextrail == "+":
                c.y -= 1
                c.intersection()
        
        elif c.direction==2:
            nextrail = rails[c.y+1][c.x]
            if nextrail == "|":
                c.y += 1
            if nextrail == "/":
                c.y += 1
                c.direction = 3
            if nextrail == "\\":
                c.y += 1
                c.direction = 1
            if nextrail == "+":
                c.y += 1
                c.intersection()
        
        elif c.direction==1:
            nextrail = rails[c.y][c.x+1]
            if nextrail == "-":
                c.x += 1
            if nextrail == "/":
                c.x += 1
                c.direction = 0
            if nextrail == "\\":
                c.x += 1
                c.direction = 2
            if nextrail == "+":
                c.x += 1
                c.intersection()
        
        elif c.direction==3:
            nextrail = rails[c.y][c.x-1]
            if nextrail == "-":
                c.x -= 1
            if nextrail == "/":
                c.x -= 1
                c.direction = 2
            if nextrail == "\\":
                c.x -= 1
                c.direction = 0
            if nextrail == "+":
                c.x -= 1
                c.intersection()

    
    for i in carts:
        matches = 0
        for j in carts:
            if i.x == j.x and i.y == j.y:
                matches += 1
        
        if matches == 2:
            print(c.x,c.y)
            running = False
            break

    """for i in range(len(rails)):
        prtline = ""
        for j in range(len(rails[i])):
            found = False
            for c in carts:
                if i == c.y and j == c.x:
                    prtline = prtline+"*"
                    found = True
                    break
            
            if not found:
                prtline = prtline+rails[i][j]
        
        print(prtline)"""
    
    
    ticks+=1

print(ticks)