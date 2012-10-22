#fibnacci is awesome.

#import math
uplimit, asum = 4000000, 0

#fiblist = [0, 1]
#while fiblist[-1] <= uplimit:
#    fiblist.append(fiblist[-2] + fiblist[-1])
#for i in fiblist:
#    if i % 2 == 0:
#        asum += i
#print(asum)

#without list.
#a, b = 1, 0
#while a <= uplimit:
#    a, b = a + b, a
#    if a % 2 == 0:
#        asum += a
#print(asum)

#fibnacci and golden ratio.
#gr = (math.sqrt(5) + 1) / 2
#print(gr)
#a, b = 1, 1
#while True:
#    print(float(a) / b)
#    a, b = a + b, a

#why bother check?
#fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...]
a, b = 2, 1
while a <= uplimit:
    asum += a
    a, b = a * 3 + b * 2, a * 2 + b
print(asum)

#fibnacci's closed-form expression
#f1, f2 = (1 + math.sqrt(5)) / 2, (1 - math.sqrt(5)) / 2
#def fib(n):
#    return int(f1 ** n / math.sqrt(5) + 0.5)
#    return int((f1 ** n - f2 ** n) / (math.sqrt(5)))

#fib(1) + fib(2) + ... + fib(n) == fib(n + 2) - 1
#fib(3 * i - 2) + fib(3 * i - 1) == fib(3 * i)
#constant time?
#does not work for large uplimits due to precision problems.
#def sumevenfibs(uplimit):
#    n = int(math.log(uplimit * math.sqrt(5) + 0.5, f1))
#    if n % 3 == 0:
#        return (fib(n + 2) - 1) / 2
#    if n % 3 == 1:
#        return (fib(n + 1) - 1) / 2
#    return (fib(n) - 1) / 2
#print(sumevenfibs(uplimit))
