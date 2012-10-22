from fractions import Fraction


def expande(k):
    mylist = []
    for i in range(1, k):
        mylist += [1, i * 2, 1]
    last = Fraction(1, mylist[k - 2])
    for i in range(k - 3, -1, -1):
        last = Fraction(1, mylist[i] + last)
    last += 2
    return last

numerator = str(expande(100)).split('/')[0]
print(sum([int(x) for x in list(numerator)]))
