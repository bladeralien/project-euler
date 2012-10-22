decimal, n = '', 1
while True:
    decimal += str(n)
    n += 1
    if len(decimal) > 1000000:
        break
temp = [int(decimal[i - 1]) for i in [1, 10, 100, 1000, 10000, 100000, 1000000]]
product = 1
for i in temp:
    product *= i
print(product)
