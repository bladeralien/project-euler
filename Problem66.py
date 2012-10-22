import math
maxminx, maxmind = 9, 5
for d in range(2, 1001):
    print(d)
    if math.sqrt(d) != int(math.sqrt(d)):
        x, y, found = 1, 1, False
        while True:
            x = math.sqrt(d * y ** 2 + 1)
            if x == int(x):
                found = True
                break
            y += 1
        if x > maxminx:
            maxminx, maxmind = x, d
print([maxminx, maxmind])
