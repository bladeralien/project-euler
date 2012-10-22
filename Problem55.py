def palindrome(n):
    return int(''.join(list(str(n))[::-1]))


def ispalindromic(n):
    return palindrome(n) == n

count = 0
for i in range(1, 10000):
    lychrel, n = True, i
    for r in range(50):
        n = n + palindrome(n)
        if ispalindromic(n):
            lychrel = False
            break
    if lychrel:
        print(i)
        count += 1
print(count)
