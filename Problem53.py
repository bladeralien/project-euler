def factorial(n):
    result = 1
    if n <= 1:
        return result
    for i in range(2, n + 1):
        result *= i
    return result


def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

count = 0
for n in range(1, 101):
    print(n)
    for r in range(0, n + 1):
        if combination(n, r) > 1000000:
            count += 1
print(count)
