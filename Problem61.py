mylist, n = [[], [], [], [], [], []], 1
while True:
    templist = [n*(n+1)/2, n*n, n*(n*3-1)/2, n*(n*2-1), n*(n*5-3)/2, n*(n*3-2)]
    for i in range(len(templist)):
        if templist[i] >= 1000 and templist[i] < 10000:
            mylist[i].append(int(templist[i]))
    if len([i for i in templist if i < 10000]) == 0:
        break
    n += 1

destlist = [[[i], [0]] for i in mylist[0]]
while True:
    templist = []
    for d in destlist:
        for m in range(1, len(mylist)):
            if m not in d[1]:
                for b in mylist[m]:
                    if str(d[0][-1])[-2:] == str(b)[:2]:
                        templist.append([d[0] + [b], d[1] + [m]])
    destlist = templist
    if len(destlist[0][0]) == 6:
        for d in destlist:
            if str(d[0][-1])[-2:] == str(d[0][0])[:2]:
                print(sum(d[0]))
                break
        break
