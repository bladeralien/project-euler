# so ugly. I hate this.

def listpro(alist):
    pro = 1
    for i in alist:
        pro *= i
    return pro

mygrid = open('Problem11.txt').readlines()
for i in range(len(mygrid)):
    mygrid[i] = [int(x) for x in mygrid[i].strip().split(' ')]

pros = []
for i in range(20):
    for k in range(17):
        pros.append(listpro(mygrid[i][k:k+4]))
for i in range(17):
    for k in range(20):
        pros.append(listpro([mygrid[i+c][k] for c in range(4)]))
for i in range(17):
    for k in range(17):
        pros.append(listpro([mygrid[i+c][k+c] for c in range(4)]))
for i in range(3, 20):
    for k in range(17):
        pros.append(listpro([mygrid[i-c][k+c] for c in range(4)]))
print(max(pros))
