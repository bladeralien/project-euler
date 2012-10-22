ciphers = [int(x) for x in open('Problem59.txt').readlines()[0].strip().split(',')]
percentages = []

for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            pwd = [a, b, c] * 400 + [a]
            original = [ciphers[i] ^ pwd[i] for i in range(len(ciphers))]
            count = 0
            for i in original:
                if i in range(65, 91) or i in range(97, 123) or i == 32 or i in range(48, 58):
                    count += 1
            percentages.append([a, b, c, float(count) / len(ciphers)])

percentages = sorted(percentages, key = lambda p: p[3])

a, b, c, per = percentages[-1]
pwd = [a, b, c] * 400 + [a]
original = [ciphers[i] ^ pwd[i] for i in range(len(ciphers))]
print(sum(original))
