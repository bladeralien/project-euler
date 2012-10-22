# Requires 9 ** n greater than 10 ** (n - 1)
count = 0
n = 1
while True:
    print(n)
    i = 1
    while len(str(i ** n)) <= n:
        if len(str(i ** n)) == n:
            print([i, n, i ** n])
            count += 1
        i += 1
    n += 1
    if n >= 22:
        break
print(count)
