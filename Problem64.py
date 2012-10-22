from decimal import *
getcontext().prec = 18
getcontext().rounding = ROUND_FLOOR
def continuedfrac(n):
    print(n)
    n = Decimal(n)
    if int(n.sqrt()) == n.sqrt():
        return [int(n.sqrt())]
    else:
        myints = [int(n.sqrt())]
        myremainders = [n.sqrt() - int(n.sqrt())]
        while True:
            temp = 1 / myremainders[-1]
            aint = int(temp)
            aremainder = temp - int(temp)
            #print([aint, aremainder])
            if aremainder not in myremainders[1:]:
                myints.append(aint)
                #print(myints)
                myremainders.append(aremainder)
                print(myremainders)
            else:
                #print(myremainders.index(aremainder))
                assert myremainders[1:].index(aremainder) == 0
                return myints

count = 0
for n in range(1, 10001):
    if len(continuedfrac(n)[1:]) % 2 == 0:
        count += 1
print(count)
