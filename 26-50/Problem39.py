maxp, maxcount = 0, 0
for perimeter in range(3, 1001):
    count = 0
    for a in range(1, perimeter - 1):
        for b in range(1, perimeter - a):
            c = perimeter - a - b
            triple = sorted([a, b, c])
            if triple[0] ** 2 + triple[1] ** 2 == triple[2] ** 2:
                count += 1
    print([perimeter, count])
    if count > maxcount:
        maxp, maxcount = perimeter, count
print(maxp)
