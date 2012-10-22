pandigits = []
for a in range(1, 10):
    for b in range(1, 10000):
        c = a * b
        if '0' not in str(b) and '0' not in str(c) and len(str(c)) == 4:
            if len(set(list(str(a)) + list(str(b)) + list(str(c)))) == 9:
                pandigits.append(c)
                print([a, b, c])
for a in range(1, 100):
    for b in range(1, 1000):
        c = a * b
        if '0' not in str(a) and '0' not in str(b) and '0' not in str(c) and len(str(c)) == 4:
            if len(set(list(str(a)) + list(str(b)) + list(str(c)))) == 9:
                pandigits.append(c)
                print([a, b, c])
print(sum(list(set(pandigits))))
