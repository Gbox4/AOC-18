class Rule:
    def __init__(self,ruleString):
        self.rule=ruleString[:5]
        self.result=ruleString[-2]

class Pot:
    def __init__(self,plantString,id):
        self.plantString=plantString
        self.neighborsState=""
        self.isZero=False
        self.id=id

class Generation:
    def __init__(self,gen,total):
        self.gen=gen
        self.total=total

#id != place in the line. it is just to give each pot a unique id
currentId=0


#   Parser      Makes rule list
rules = []
f=open("day12input.txt","r")
contents=f.readlines()
initial = None
for i in range(len(contents)):
    if i == 0:
        initial = contents[i][15:-2]
    elif i >= 2:
        rules.append(Rule(contents[i]))

#Makes pot list
pots = []
for i in initial:
    pots.append(Pot(i,currentId))
    currentId+=1

pots[0].isZero=True


#Gets state of neighboring pots
def getNeighbors(pots):
    for i in range(len(pots)):
        neighborStr=""
        for j in range(-2,3):
            offset = i+j
            if offset < 0 or offset >= len(pots):
                neighborStr+="."
            else:
                neighborStr+=pots[offset].plantString

        pots[i].neighborsState=neighborStr

#checks if it is necessary to add pots to either end
def checkEnds():
    needsAdding=[]
    for r in rules:
        if r.result=="#":
            

            if "."+pots[0].neighborsState[:4]==r.rule:
                needsAdding.append(-1)
            if ".."+pots[0].neighborsState[:3]==r.rule:
                needsAdding.append(-2)
            if pots[0].neighborsState[1:]+"."==r.rule:
                needsAdding.append(1)
            if pots[0].neighborsState[2:]+".."==r.rule:
                needsAdding.append(2)
    
    return (needsAdding)



#Calculates a generation
def generate():
    global currentId

    for i in range(2):
        pots.append(Pot(".",currentId))
        currentId+=1
        pots.insert(0,Pot(".",currentId))
        currentId+=1

    ends = checkEnds()
    if -2 in ends:
        for i in range(2):
            pots.insert(0,Pot(".",currentId))
            currentId+=1
    elif -1 in ends:
        pots.insert(0,Pot(".",currentId))
        currentId+=1

    if 2 in ends:
        for i in range(2):
            pots.append(Pot(".",currentId))
            currentId+=1
    elif 1 in ends:
        pots.append(Pot(".",currentId))
        currentId+=1


    getNeighbors(pots)

    for p in pots:
        for r in rules:
            if p.neighborsState == r.rule:
                p.plantString = r.result

getNeighbors(pots)

#Gets index of a pot from id
def getPotRelativeIndex(potid):
    potIndex=None
    zeroIndex=None
    for p in range(len(pots)):
        if pots[p].id==potid:
            potIndex=p
        
        if pots[p].isZero:
            zeroIndex=p
    
    return(potIndex-zeroIndex)

def calcTotal():
    total=0
    for i in pots:
        
        if i.plantString=="#":
            total+=getPotRelativeIndex(i.id)
    return(total)

gens = []

genNum = 0
for i in range(200):
    generate()
    gens.append(Generation(genNum,calcTotal()))
    genNum+=1

firstTotal=gens[1].total

difs=[]
for i in range(1,len(gens)):
    try:
        dif = gens[i].total-gens[i-1].total
        #if dif in difs:
        print("generation: {0}      difference: {1}          total: {2}".format(i+1,dif,gens[i].total))
        #else:
            #difs.append(dif)
    except:
        break







print("Program End.")