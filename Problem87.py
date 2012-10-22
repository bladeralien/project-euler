primes = [int(line.strip()) for line in open('Primes.txt').readlines()]
primesa = [ap for ap in primes if ap < 50000000 ** (float(1)/2)]
primesb = [ap for ap in primes if ap < 50000000 ** (float(1)/3)]
primesc = [ap for ap in primes if ap < 50000000 ** (float(1)/4)]

tempset = set([])
for a in primesa:
    for b in primesb:
        for c in primesc:
            temp = a ** 2 + b ** 3 + c ** 4
            if temp < 50000000:
                tempset.add(temp)
print(len(tempset))
