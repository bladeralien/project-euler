import Primes


def lcm(integerlist):
    """
    lcm stands for least common multiple.
    this function calculate the lcm of some integers.
    """
    lcmdict = {}
    for i in integerlist:
        factorslist = Primes.factors(i)
        factorsdict = {}
        for k in factorslist:
            factorsdict.setdefault(k, 0)
            factorsdict[k] += 1
        for afactor in factorsdict:
            lcmdict.setdefault(afactor, 0)
            if lcmdict[afactor] < factorsdict[afactor]:
                lcmdict[afactor] = factorsdict[afactor]
    mylcm = 1
    for afactor in lcmdict:
        mylcm *= afactor ** lcmdict[afactor]
    return mylcm, lcmdict

#for k in range(20, 100):
#    print([k, lcm(range(2, k + 1))])
#print(lcm(range(2, 100000 + 1)))
#print(lcm(range(100, 110)))

import math
def continuouslcm(n):
    result = 1
    for ap in Primes.primes:
        if ap <= n:
            result *= ap ** int(math.log(n, ap))
    return result
print(continuouslcm(10 ** 6))
        
