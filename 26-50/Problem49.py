primes = [int(line.strip()) for line in open('Primes.txt').readlines()]
primes = [ap for ap in primes if ap < 10000]

for i in range(1000, 3340):
    a, b, c = i, i + 3330, i + 2 * 3330
    if a in primes and b in primes and c in primes:
        if len(set(list(''.join([str(x) for x in [a, b, c]])))) == 3:
            print([a, b, c]) # this will print [2969, 6299, 9629].
        if len(set(list(''.join([str(x) for x in [a, b, c]])))) == 4:
            print([a, b, c]) # this will print [1487, 4817, 8147].
