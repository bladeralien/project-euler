import math
import Primes

noprime, noall = 0, 1
diagonals = [[1]]
while True:
    current = diagonals[-1]
    step = len(diagonals) * 2
    diagonals.append([current[-1] + (i + 1) * step for i in range(4)])
    for i in diagonals[-1]:
        if Primes.isPrime(i):
            noprime += 1
    noall += len(diagonals[-1])
    percentage = float(noprime) / noall
    if percentage < 0.1:
        break
print(math.sqrt(diagonals[-1][-1]))
