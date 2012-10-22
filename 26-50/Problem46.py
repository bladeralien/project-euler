def isSquare(n):
    import math
    return int(math.sqrt(n)) == math.sqrt(n)

primes = [int(line.strip()) for line in open('Primes.txt').readlines()][1:]

n = 33
while True:
    temp = False
    for ap in primes:
        if n - ap >= 0:
            if isSquare((n - ap) / 2):
                temp = True
    if temp == False:
        print(n)
        break
    n += 2
