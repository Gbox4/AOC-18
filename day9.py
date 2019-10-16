#Gabe Banks
#2/27/19

#puzzle = "452 players; last marble is worth 71250 points"
puzzle = "10 players; last marble is worth 1618 points: high score is 8317"

#how many players
playercount = 452
#how many marbles
marblescount = 71250

#check if divisible by 23
def specialMarble(marbn):
    if marbn%23 == 0:
        return True
    else:
        return False



#linked list
class linkedListElement:
    def __init__(self,val,linkedlist, prev, fol):
        self.linkedlist = linkedlist
        self.val=val
        self.prev = prev
        self.fol = fol


#player datastucture
class player:
    def __init__(self, id, points):
        self.id = id
        self.points = points

#list of all players
players = []

for i in range(playercount):
    players.append(player(i, 0))


#list of remaining marbles
marbles = []
for i in range(marblescount):
    marbles.append(i+1)

print("marble list done")

#circle of marbles
circle = [0]

incomplete = True
position = 0
while incomplete:
    
    for p in players:
        position += 2

        if marbles[0] % 23 == 0:
            p.points += marbles[0]
            marbles = marbles[1:]

            position -= 9
            if position < 0:
                position += len(circle)
            
            p.points += circle[position]
            circle = circle[:position] + circle[position+1:]

#-7, if <0 add len
        elif position == len(circle):
            circle.append(marbles[0])
            marbles = marbles[1:]
        
        elif position > len(circle):
            position -= len(circle)
            circle = circle[:position] + [marbles[0]] + circle[position:]
            marbles = marbles[1:]
        
        else:
            circle = circle[:position] + [marbles[0]] + circle[position:]
            marbles = marbles[1:]

        if len(marbles) == 0:
            break
    
    if len(marbles) == 0:
            break


highest = 0
for i in players:
    if highest < i.points:
        highest = i.points

print(highest)