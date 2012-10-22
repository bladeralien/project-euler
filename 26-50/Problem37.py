primes = [int(line.strip()) for line in open('Primes.txt').readlines()]
truncatableprimes = []
for ap in primes[4:]:
    print(ap)
    truncatable = True
    strform = str(ap)
    for i in range(1, len(strform)):
        if int(strform[i:]) not in primes or int(strform[:i]) not in primes:
            truncatable = False
            break
    if truncatable == True:
        truncatableprimes.append(ap)
for i in truncatableprimes:
    print(i)
