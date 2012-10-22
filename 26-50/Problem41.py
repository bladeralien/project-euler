import itertools
import Primes

# awesome.
# 1+2+3+4+5+6+7+8+9=45
# 1+2+3+4+5+6+7+8=36

for aper in itertools.permutations(range(7, 0, -1)):
    candidate = int(''.join([str(x) for x in list(aper)]))
    if Primes.isPrime(candidate):
        print(candidate)
        break
