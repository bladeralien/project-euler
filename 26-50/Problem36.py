def bin(n):
    assert type(n) == type(1)
    result = ''
    while n != 0:
        result = str(n % 2) + result
        n =n / 2
    return result

asum = 0
for i in range(1000000):
    if i == int(''.join(list(str(i))[::-1])):
        binform = bin(i)
        if binform == ''.join(list(binform)[::-1]):
            print(i)
            asum += i
print(asum)
