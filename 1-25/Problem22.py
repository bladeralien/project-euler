names = [name[1:-1] for name in 
         open('Problem22.txt').readlines()[0].strip().split(',')]
names.sort()
sums = 0
for i in range(len(names)):
    name = names[i]
    score = 0
    for achar in name:
        score += ord(achar) - 64
    score *= (i + 1)
    sums += score
print(sums)
