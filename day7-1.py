#GNPFBHACMVEWQRUDSIZJYTKOLX
import string

class Step:
    def __init__(self, name):
        self.name = name
        self.time = string.ascii_uppercase.index(name)+1

    def printInfo(self):
        print(self.name,self.time)

class Worker:
    def __init__(self):
        self.working = False
        self.workingOn = None

test = "CABFDE"

code = []

for i in test:
    code.append(Step(i))

workers = []

for i in range(2):
    workers.append(Worker())

onStep = 0
latestJob = 

while True:
    if onStep == len(test)-1:
        break
    
    for i in range(onStep, len(test)):
        for j in workers:
            if j.working
    


print()