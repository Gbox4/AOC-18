#linked list
class linkedListElement:
    def __init__(self,val, prev, fol):
        self.val=val
        self.prev = prev
        self.fol = fol
    
    def loop(self):
        if self.prev != None:
            self.prev.loop()
            return(self.val)
        
        else:
            return(self.val)

#make linked list from list
def constructLinkedList(olist):
    lliste=[]
    for i in range(len(olist)):
        lliste.append(linkedListElement(olist[i],None,None))
    

    for i in range(len(lliste)):
        test=len(lliste)-1
        if i==0:
            lliste[i].prev=None
            lliste[i].fol=lliste[i+1]


        elif i < test and i != 0:
            lliste[i].prev=lliste[i-1]
            lliste[i].fol=lliste[i+1]
        else:
            lliste[i].prev=lliste[i-1]
            lliste[i].fol=None
    
    return(lliste[len(lliste)-1])
    
test=[1,2,3,4,5]

llist = constructLinkedList(test)
print(llist.loop())