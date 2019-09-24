test =  """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

puzzle = """Step G must be finished before step N can begin.
Step N must be finished before step B can begin.
Step P must be finished before step Q can begin.
Step F must be finished before step U can begin.
Step H must be finished before step A can begin.
Step C must be finished before step S can begin.
Step A must be finished before step K can begin.
Step M must be finished before step O can begin.
Step V must be finished before step L can begin.
Step E must be finished before step L can begin.
Step B must be finished before step Q can begin.
Step W must be finished before step J can begin.
Step R must be finished before step D can begin.
Step D must be finished before step S can begin.
Step S must be finished before step X can begin.
Step Q must be finished before step J can begin.
Step I must be finished before step L can begin.
Step U must be finished before step J can begin.
Step Z must be finished before step X can begin.
Step Y must be finished before step T can begin.
Step J must be finished before step K can begin.
Step T must be finished before step L can begin.
Step K must be finished before step O can begin.
Step O must be finished before step X can begin.
Step L must be finished before step X can begin.
Step Y must be finished before step O can begin.
Step F must be finished before step S can begin.
Step K must be finished before step L can begin.
Step Z must be finished before step O can begin.
Step J must be finished before step X can begin.
Step K must be finished before step X can begin.
Step Q must be finished before step X can begin.
Step Y must be finished before step L can begin.
Step E must be finished before step S can begin.
Step H must be finished before step Y can begin.
Step G must be finished before step P can begin.
Step E must be finished before step K can begin.
Step B must be finished before step L can begin.
Step T must be finished before step K can begin.
Step N must be finished before step R can begin.
Step F must be finished before step E can begin.
Step W must be finished before step Y can begin.
Step U must be finished before step X can begin.
Step A must be finished before step I can begin.
Step Q must be finished before step Y can begin.
Step P must be finished before step T can begin.
Step D must be finished before step X can begin.
Step E must be finished before step Y can begin.
Step F must be finished before step B can begin.
Step P must be finished before step I can begin.
Step N must be finished before step S can begin.
Step F must be finished before step V can begin.
Step W must be finished before step U can begin.
Step F must be finished before step A can begin.
Step I must be finished before step Z can begin.
Step E must be finished before step D can begin.
Step R must be finished before step I can begin.
Step M must be finished before step V can begin.
Step R must be finished before step U can begin.
Step R must be finished before step X can begin.
Step G must be finished before step O can begin.
Step G must be finished before step H can begin.
Step M must be finished before step R can begin.
Step E must be finished before step U can begin.
Step F must be finished before step Z can begin.
Step N must be finished before step Q can begin.
Step U must be finished before step O can begin.
Step J must be finished before step T can begin.
Step W must be finished before step Z can begin.
Step I must be finished before step J can begin.
Step U must be finished before step L can begin.
Step I must be finished before step X can begin.
Step Z must be finished before step J can begin.
Step F must be finished before step D can begin.
Step N must be finished before step O can begin.
Step Q must be finished before step U can begin.
Step G must be finished before step L can begin.
Step H must be finished before step Q can begin.
Step M must be finished before step Q can begin.
Step N must be finished before step D can begin.
Step Z must be finished before step L can begin.
Step I must be finished before step Y can begin.
Step E must be finished before step X can begin.
Step J must be finished before step L can begin.
Step H must be finished before step W can begin.
Step P must be finished before step Y can begin.
Step Q must be finished before step T can begin.
Step Z must be finished before step Y can begin.
Step R must be finished before step T can begin.
Step E must be finished before step J can begin.
Step I must be finished before step T can begin.
Step A must be finished before step L can begin.
Step E must be finished before step R can begin.
Step T must be finished before step O can begin.
Step Y must be finished before step X can begin.
Step A must be finished before step Q can begin.
Step W must be finished before step Q can begin.
Step A must be finished before step T can begin.
Step B must be finished before step Y can begin.
Step H must be finished before step E can begin.
Step H must be finished before step K can begin."""

code = puzzle.split("\n")

class Step:
    def __init__(self, name):
        self.finished = False
        self.reqs = []
        self.name = name

steps = []

def existsStep(step,steps):
    for i in steps:
        if i.name == step:
            return True
    
    return False

def getStep(step,steps):
    for i in steps:
        if i.name == step:
            return i

def parse(line):
    return [line[5], line[36]]

steps = []

for l in code:
    name = parse(l)[1]
    req = parse(l)[0]
    if not existsStep(name, steps):
        steps.append(Step(name))
    
    if not existsStep(req, steps):
        steps.append(Step(req))
    
    name = getStep(name, steps)
    req = getStep(req, steps)

    name.reqs.append(req)

def sortSteps(steps):
    stepNames = []
    for i in steps:
        stepNames.append(i.name)
    
    sortedSteps = []
    stepNames.sort()

    for i in stepNames:
        sortedSteps.append(getStep(i,steps))
    
    return sortedSteps


    

found = True

order = []

while found:
    exeList = []
    found = False
    for i in steps:
        if i.finished:
            continue

        canExecute = True
        for r in i.reqs:

            if not r.finished:
                canExecute = False
                break
        
        if canExecute:
            found = True
            exeList.append(i)
    
    if len(exeList) != 0:
        exeList = sortSteps(exeList)
        order.append(exeList[0].name)
        exeList[0].finished = True

final = ""
for i in order:
    final = final + i

print(final)

#GNPFBHACMVEWQRUDSIZJYTKOLX