def factorial(n):
    temp = 1
    for i in range(2, n + 1):
        temp *= i
    return temp

count = 0
for i in range(1, 1000000):
    print(i)
    temp, templist = i, [i]
    while True:
        temp = sum([factorial(n) for n in [int(x) for x in list(str(temp))]])
        if temp not in templist:
            templist.append(temp)
        else:
            break
    if len(templist) == 60:
        count += 1
print(count)
