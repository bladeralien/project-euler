myprimes = [2, 3, 5, 7, 11, 13, 17]
mylist = []
for ap in myprimes:
    templist = []
    for i in range(1000):
        if i % ap == 0:
            tempstr = str(i)
            while len(tempstr) < 3:
                tempstr = '0' + tempstr
            templist.append(tempstr)
    mylist.append(templist)

destlist = mylist[0]
for i in range(1, len(mylist)):
    templist = []
    for m in destlist:
        for n in mylist[i]:
            if m[-2:] == n[:-1]:
                tempstr = m + n[-1]
                if len(set(list(tempstr))) == len(m) + len(n) - 2:
                    templist.append(tempstr)
    destlist = templist

finallist = []
for d in destlist:
    for i in range(10):
        if str(i) not in d:
            finallist.append(int(str(i) + d))
            break
print(sum(finallist))
