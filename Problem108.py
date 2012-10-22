#n = 2
#while True:
#    print(n)
#    count, y = 0, n + 1
#    while True:
#        x = float(n * y) / (y - n)
#        if x <= n:
#            break
#        if int(x) == x:
#            count += 1
#        y += 1
#    if count > 1000:
#        print(n)
#        break
#    n += 1



n = 1
while True:
    print(n)
    count = 0
    for y in range(n + 1, n * 2 + 1):
        x = float(n * y) / (y - n)
        if int(x) == x:
            count += 1
    print([n, count])
    if count > 1000:
        print(n)
        break
    n += 1
