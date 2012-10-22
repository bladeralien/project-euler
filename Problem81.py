source = [line.strip().split(',') for line in open('Problem81.txt').readlines()]
source = [[int(x) for x in line] for line in source]


def minimalpath(a, b, memory):
    if (a, b) in memory:
        return memory[(a, b)]
    if a == 0:
        result = sum([source[a][i] for i in range(b + 1)])
    elif b == 0:
        result = sum([source[i][b] for i in range(a + 1)])
    else:
        tempa = minimalpath(a - 1, b, memory)
        tempb = minimalpath(a, b - 1, memory)
        result = min(tempa, tempb) + source[a][b]
    memory[(a, b)] = result
    return result

print(minimalpath(79, 79, {}))
