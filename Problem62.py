i, mydict = 1, {}
while True:
    print(i)
    temp = i ** 3
    tempstr = ''.join(sorted(list(str(temp))))
    mydict.setdefault(tempstr, [0, []])
    mydict[tempstr][0] += 1
    mydict[tempstr][1].append(temp)
    if mydict[tempstr][0] == 5:
        print(mydict[tempstr])
        break
    i += 1
