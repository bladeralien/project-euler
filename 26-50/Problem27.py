# use set.
primes = set([int(line.strip()) for line in open('Primes.txt').readlines()])

consecutives = []
blist = [ap for ap in primes if ap < 1000]
for a in range(-999, 1000):
    for b in blist:
        temp = max(abs(b), abs(a - b))
        if temp >= 40:
            consecutives.append([a, b, temp])

i = 40
while len(consecutives) > 1:
    print(len(consecutives))
    templist = []
    for t in consecutives:
        a, b, temp = t
        if i * i + a * i + b in primes:
            templist.append([a, b, i])
    consecutives = templist
    i += 1
print(consecutives)
