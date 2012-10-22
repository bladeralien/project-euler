#tempset = set([])
#for d in range(2, 1000001):
#    print(d)
#    for n in range(1, d):
#        tempset.add(float(n)/d)
#print(len(tempset))
##tempset = set([])
##import Primes
#primes = [int(line.strip()) for line in open('Primes.txt').readlines()]
#primes = [ap for ap in primes if ap <= 1000000]
#count = 0
#for d in range(2, 1000001):
#    print(d)
#    for n in range(1, d):
#        nprime2d = True
#        for ap in primes:
#            if n % ap == 0 and d % ap == 0:
#                nprime2d = False
#                break
#        if nprime2d == True:
#            count += 1
#print(count)


##print(Primes.factors(2))
##print(Primes.factors(20))
##print(Primes.factors(37))
#count = 0
#for d in range(2, 1000001):
#    print(d)
#    tempset = set([])
#    for f in set(Primes.factors(d)):
#        i = 1
##        while f * i < d:
##            tempset.add(f * i)
##            i += 1
##    count += d - 1 - len(tempset)
##print(count)
##print(sum(primes) - len(primes)
#count = 0
#for ap in primes:
#    print(ap)
#    templist, i = [], 2
#    while ap * i <= 1000000:
#        templist.append(ap * i)
#        i += 1
#    count += 1000000 - ap - len(templist)
#print(count + 1000000 - 1)
count = 0
for n in range(2, 1000000):
    count += 1000000 - int(1000000 / n) - (n - 1)
count += 1000000 - 1
print(count)
    
# The easy way.
# 3 / 7 = (3 * 142857) / (7 * 142857) = 428571 / 999999
# The hard way.
##import math
##immediatelyn, immediatelyd, immediately = 2, 5, float(2)/5
##for d in range(2, 1000001):
##    print(d)
##    for n in range(int(float(d)*immediatelyn/immediatelyd)+1, int(math.ceil(float(d)*3/7))):
##        if float(n)/d > immediately:
##            immediatelyn, immediatelyd, immediately = n, d, float(n)/d
##print([immediatelyn, immediatelyd])
