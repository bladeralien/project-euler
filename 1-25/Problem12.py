from math import sqrt


def nofactors(n):
    factors = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n/i)
    return len(factors)

n = 1
while True:
    triangle = sum(range(n)) + n
    #print(str(triangle) + '\t' + str(nofactors(triangle)))
    if nofactors(triangle) > 500:
        print(triangle)
        break
    n += 1
