source = [line.strip().split(',') for line in open('Problem82.txt').readlines()]
source = [[int(x) for x in line] for line in source]


def minimalpath(b):
    print(b)
    column2 = [source[a][b] for a in range(len(source))]
    if b == 0:
        return column2
    result, column1 = [], minimalpath(b - 1)
    for m in range(len(column2)):
        temp = []
        for n in range(len(column1)):
            if n < m:
                for k in range(n, m + 1):
                    temp.append(sum(column1[n:k+1] + column2[k:m+1]))
            if n == m:
                temp.append(column1[n] + column2[m])
            if n > m:
                for k in range(n, m - 1, -1):
                    temp.append(sum(column1[k:n+1] + column2[m:k+1]))
        result.append(min(temp))
    print(b)
    return result
print(min(minimalpath(len(source) - 1)))
