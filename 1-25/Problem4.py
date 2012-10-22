#palindrome = []
#for a in range(100, 1000):
#    for b in range(a, 1000):
#        product = a * b
#        if int(str(product)[::-1]) == product:
#            palindrome.append(product)
#palindrome.sort()
#print(palindrome[-1])

#without list.
#maxpali = 10000
#for a in range(999, 99, -1):
#    for b in range(a, 99, -1):
#        product = a * b
#        if product <= maxpali:
#            break
#        if int(str(product)[::-1]) == product:
#            maxpali = product
#print(maxpali)

def maxpalindrome(d):
    maxpali = 0
    for a in range(10 ** d - 1, 10 ** (d - 1) - 1, -1):
        for b in range(a, 10 ** (d - 1) - 1, -1):
            product = a * b
            if product <= maxpali:
                break
            if int(str(product)[::-1]) == product:
                maxpali = product
    return maxpali
print(maxpalindrome(3))

#there always exists a better way.
