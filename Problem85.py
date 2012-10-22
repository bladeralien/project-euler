##def myfunc(m, n):
##    temp = 0
##    for a in range(1, m + 1):
##        for b in range(1, n + 1):
##            temp += a * b
##    return temp
def myfunc(m, n):
    return m * (m + 1) * n * (n + 1) / 4
minm, minn, mindiff = 1, 1, 2000000
for m in range(1, 2001):
    for n in range(1, 2001):
        temp = myfunc(m, n)
        if abs(temp - 2000000) < mindiff:
            minm, minn, mindiff = m, n, abs(temp - 2000000)
print([minm, minn, mindiff])
