maxa, maxb, maxsum = 1, 1, 1
for a in range(1, 100):
    for b in range(1, 100):
        temp = sum([int(x) for x in list(str(a ** b))])
        if temp > maxsum:
            maxa, maxb, maxsum = a, b, temp
print([maxa, maxb, maxsum])
