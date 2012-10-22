import math
d = 10 ** 12 + 1
found = False
while True:
    if d % 10000 == 0:
        print(d)
    tempd = d * (d - 1) / 2
    b = int(math.sqrt(tempd)) + 1
    while True:
        tempb = b * (b - 1)
        if tempb == tempd:
            found = True
            break
        if tempb > tempd:
            break
        b += 1
    if found == True:
        print([b, d])
        break
    d += 1
