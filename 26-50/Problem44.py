# This could be more elegant.

pentagonals = []
for i in range(1, 5000):
    pentagonals.append(i * (i * 3 - 1) / 2)
pentagonalssets = set(pentagonals)

mina, minb = pentagonals[0], pentagonals[-1]
mindiff = pentagonals[-1] - pentagonals[0]
check = 4999

for n in range(check - 1):
    for k in range(n + 1, check):
        a, b = pentagonals[n], pentagonals[k]
        if a + b in pentagonalssets and b - a in pentagonalssets:
            if b - a < mindiff:
                mina, minb, mindiff = a, b, b - a
print([mina, minb, mindiff])
