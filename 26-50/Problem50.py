primes = [int(line.strip()) for line in open('Primes.txt').readlines()]
primesset = set(primes)
maxlenprime, maxlen = 953, 21

for i in range(len(primes) - 1):
    k = i
    while True:
        k += 1
        if sum(primes[i: k + 1]) > 1000000:
            break
        if sum(primes[i: k + 1]) in primesset:
            if k - i + 1 > maxlen:
                maxlenprime, maxlen = sum(primes[i: k + 1]), k - i + 1
                print([maxlenprime, maxlen, primes[i: k + 1]])
