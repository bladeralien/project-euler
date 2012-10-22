triangle = [line.strip().split(' ') for line in open('Problem18.txt').readlines()]
triangle = [[int(x) for x in i] for i in triangle]
for row in range(len(triangle) - 2, -1, -1):
    for col in range(len(triangle[row])):
        triangle[row][col] += max(triangle[row+1][col], triangle[row+1][col+1])
print(triangle[0][0])
