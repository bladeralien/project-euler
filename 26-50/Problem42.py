words = open('Problem42.txt').readlines()
words = [word[1:-1] for word in words[0].strip().split(',')]

triangles = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378]

count = 0
for word in words:
    value = 0
    for achar in word:
        value += ord(achar) - 64
    if value in triangles:
        print(word)
        count += 1
print(count)
