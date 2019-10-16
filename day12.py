f=open("day12input.txt","r")
contents=f.readlines()
initial = None
for i in range(len(contents)):
    if i == 1:
        initial = contents[i][15:]
    elif i >= 3:
        pass

print(initial)