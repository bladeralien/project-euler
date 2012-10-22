import Collections
myfib, k = Collections.Fibs(), 2749
print(myfib[k])
while True:
    print(k)
    strtemp = str(myfib[k])
    if '.'.join(sorted(strtemp[:9])) == '123456789' and '.'.join(sorted(strtemp[-9:])) == '123456789':
        print([k, myfib[k]])
        break
    k += 1
