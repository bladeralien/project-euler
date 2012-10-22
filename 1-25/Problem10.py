import Primes
Primes.extendTo(2000000)
print(sum([int(line.strip()) for line in open('Primes.txt').readlines()]))
