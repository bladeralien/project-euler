def lenchain(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    return lenchain(n) + 1

maxlen, startno = 1, 1
for i in range(1, 1000000):
    if lenchain(i) > maxlen:
        maxlen, startno = lenchain(i), i
print(startno)
