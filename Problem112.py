def increasing(n):
    templist = [int(x) for x in list(str(n))]
    for i in range(1, len(templist)):
        if templist[i] < templist[i - 1]:
            return False
    return True


def decreasing(n):
    templist = [int(x) for x in list(str(n))]
    for i in range(1, len(templist)):
        if templist[i] > templist[i - 1]:
            return False
    return True


def bouncy(n):
    if n < 100:
        return False
    return not increasing(n) and not decreasing(n)


temp, count = 1, 0
while True:
    print(temp)
    if bouncy(temp):
        count += 1
    if count * 100 == temp * 99:
        print([count, temp])
        break
    temp += 1
