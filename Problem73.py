import math
tempset = set([])
for d in range(7, 12001):
    for n in range(math.floor(d/3)+1, math.ceil(d/2)):
        tempset.add(float(n)/d)
print(len(tempset))
