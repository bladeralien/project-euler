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

abundants = []
for i in range(1, 28124):
    if sum(factors(i)) > i:
        abundants.append(i)
#print(abundants)

templist = [a + b for a in abundants for b in abundants if a + b < 28124]
print(sum(list(set(range(1, 28124)).difference(set(templist)))))
