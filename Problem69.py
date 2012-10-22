import Primes
primesset = set([ap for ap in Primes.primes if ap <= 1000000])

# Oh, I am so genius.
temp = 1
for ap in Primes.primes:
    temp *= ap
    if temp > 1000000:
        print(temp / ap)
        break

# Brure force way, may take several days.
maxn, maxn2phi = 6, 3
for n in range(2, 1000001):
    if n not in primesset:
        phi = 0
        for r in range(1, n):
            relativeprime = True
            for ap in Primes.primes:
                if r % ap == 0 and n % ap == 0:
                    relativeprime = False
                    break
            if relativeprime == True:
                phi += 1
        n2phi = float(n) / phi
        print([n, phi, n2phi])
        if n2phi > maxn2phi:
            maxn, maxn2phi = n, n2phi
