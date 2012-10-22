import math
source = [line.strip().split(',') for line in open('Problem99.txt').readlines()]
maxa, maxb, maxpow = 0, 0, 0
for line in source:
    a, b = line
    temp = int(b) * math.log(int(a))
    if temp > maxpow:
        maxa, maxb, maxpow = a, b, temp
print([maxa, maxb, maxpow])
