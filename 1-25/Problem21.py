#Still a little messy here.

from math import sqrt


def factors(n):
    factorslist = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factorslist.append(i)
            factorslist.append(n/i)
    factorslist = list(set(factorslist))
    factorslist.sort()
    factorslist = [f for f in factorslist if f < n]
    return factorslist

amicables = []
for i in range(1, 10000):
    sumfactors = sum(factors(i))
    if sumfactors != i and sum(factors(sumfactors)) == i:
        amicables += [i, sumfactors]
amicables = list(set(amicables))
amicables.sort()
print(sum(amicables))
