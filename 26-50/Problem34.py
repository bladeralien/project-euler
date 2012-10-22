def factorial(n):
    """Please make sure that n is greater than or equal to zero."""
    temp = 1
    for i in range(1, n + 1):
        temp *= i
    return temp

for i in range(3, 3000000):
    if sum([factorial(int(x)) for x in list(str(i))]) == i:
        print(i)
