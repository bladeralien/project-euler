#asum = 0
#for i in range(1000):
#    if i % 3 == 0 or i % 5 == 0:
#        asum += i
#print(asum)

#i, asum = 1, 0
#while i < 1000000000:
#    if i % 3 == 0 or i % 5 == 0:
#        asum += i
#    i += 1
#print(asum)

import math
import itertools

#def summultiples(bound, a, b):
#    ua, ub = math.ceil(float(bound)/a)-1, math.ceil(float(bound)/b)-1
#    c = a*b
#    uc = math.ceil(float(bound)/(c))-1
#    result = ((1 + ua) * ua * a + (1 + ub) * ub * b - (1 + uc) * uc * c) / 2
#    return result
#print(int(summultiples(1000000000, 3, 5)))

def summultiples(bound, multiplicands):
    count, result = 0, 0
    for i in range(1, len(multiplicands) + 1):
        for c in itertools.combinations(multiplicands, i):
            multiplicand = reduce((lambda x, y: x * y), c, 1)
            temp = math.ceil(float(bound)/multiplicand)-1
            result += (-1) ** (i%2+1) * (1+temp) * temp * multiplicand / 2
            count += (-1) ** (i%2+1) * temp
    return [count, int(result)]
print(summultiples(1000000000, [3, 5]))
print(summultiples(100, [3, 4, 7]))
