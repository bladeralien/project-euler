import Primes

n = 1
while True:
    found = True
    if n % 100 == 0:
        print(n)
        print(Primes.factors(n + 1))
    step = 0
    for i in range(n, n + 4):
        tempset = set(Primes.factors(i))
        if len(tempset) != 4:
            found = False
            step = i - n
            break
    if found == True:
        print(n)
        break
    n += step + 1
