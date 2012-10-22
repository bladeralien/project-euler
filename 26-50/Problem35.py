def circular(n):
    strform = list(str(n))
    templist = []
    for k in range(1, len(strform)):
        templist.append(int(''.join(strform[k:] + strform[:k])))
    return templist


primes = [int(line.strip()) for line in open('Primes.txt').readlines()]
candidates = [ap for ap in primes if ap < 1000000]
circularprimes = []
for ap in candidates:
    iscircular = True
    for ac in circular(ap):
        if ac not in candidates:
            iscircular = False
            break
    if iscircular:
        circularprimes.append(ap)
print(len(circularprimes))
