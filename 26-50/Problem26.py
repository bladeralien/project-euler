def mydivide(numerator, denominator):
    quotients = []
    remainders = []
    while True:
        quotient = numerator / denominator
        remainder = numerator % denominator
        quotients.append(quotient)
        remainders.append(remainder)
        numerator = remainder * 10
        if remainder == 0:
            strquotients = [str(x) for x in quotients]
            return strquotients[0] + '.' + ''.join(strquotients[1:])
        if remainder in remainders[:-1]:
            border = remainders.index(remainder) + 1
            strquotients = [str(x) for x in quotients]
            return(strquotients[0] + '.' + ''.join(strquotients[1:border]) +
                   '(' + ''.join(strquotients[border:]) + ')')

maxd, maxlen = 2, 0
for d in range(2, 1000):
    quotients = mydivide(1, d)
    cyclepart = quotients[quotients.find('(') + 1: quotients.find(')')]
    if len(cyclepart) > maxlen:
        maxd, maxlen = d, len(cyclepart)
print(str(maxd) + '\t' + str(maxlen))
