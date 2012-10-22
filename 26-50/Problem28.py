import math

diagonals = [[1]]
while math.sqrt(diagonals[-1][-1]) < 1001:
    current = diagonals[-1]
    step = len(diagonals) * 2
    diagonals.append([current[-1] + (i + 1) * step for i in range(4)])
print(diagonals)

asum = 0
for spiral in diagonals:
    for i in spiral:
        asum += i
print(asum)
