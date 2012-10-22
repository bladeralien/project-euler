from fractions import Fraction
frac = Fraction(1, 2 + Fraction(1, 2))

count = 0
for i in range(3, 1001):
    frac = Fraction(1, 2 + frac)
    numerator, denominator = str(1 + frac).split('/')
    if len(numerator) > len(denominator):
        #print(1 + frac)
        count += 1
print(count)
