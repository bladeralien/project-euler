#so messy.

from math import sqrt
#import os
#os.chdir('/media/Life/ProjectEuler/')

primes = [int(line[:-1]) for line in open('Primes.txt').readlines()]
primesset = set(primes)


def isPrime(i):
    if i <= 1:
        return False
    temp = int(sqrt(i))
    for ap in primes:
        if ap <= temp:
            if i % ap == 0:
                return False
        else:
            break
    k = primes[-1] + 2
    while k <= temp:
        if i % k == 0:
            return False
        k += 2
    return True


#def isPrime(i):
#    """
#    Please make sure that there is enough primes in the txt file.
#    """
#    if i <= 1:
#        return False
#    if i > primes[-1]:
#        extendTo(i)
#    return i in primesset


def extendTo(i):
    print('Extending...')
    dest = file('Primes.txt', 'a')
    k = primes[-1] + 2
    while k <= i:
        if isPrime(k):
            primes.append(k)
            primesset.add(k)
            dest.write(str(k) + '\n')
        k += 2
    dest.close()


def factors(i):
    factorlist = []
    for ap in primes:
        while i % ap == 0:
            i /= ap
            factorlist.append(ap)
        if i == 1:
            return factorlist
    if isPrime(i):
        factorlist.append(i)
        return factorlist
    currentlen = len(primes)
    extendTo(int(sqrt(i)))
    for ap in primes[currentlen:]:
        while i % ap == 0:
            i /= ap
            factorlist.append(ap)
        if i == 1:
            return factorlist
#
#
#
#    factorlist = []
#    while True:
#        for ap in primes:
#            if i % ap == 0:
#                i /= ap
#                factorlist.append(ap)
#        if isPrime(i):
#            factorlist.append(i)
#            break
#        if i == 1:
#            break
#    factorlist.sort()
#    return factorlist
