for i in range(1010101000, 1389026700, 100):
    print(i)
    foundA, foundB, tempstrA, tempstrB = True, True, str((i + 30) ** 2), str((i + 70) ** 2)
    for i in range(0, 9):
        if tempstrA[i * 2] != str(i + 1):
            foundA = False
            break
    for i in range(0, 9):
        if tempstrB[i * 2] != str(i + 1):
            foundB = False
            break
    if foundA == True or foundB == True:
        print([i, i ** 2])
        break

#candidate = ['0']
#for a in range(0, -9, -1):
#    print(a)
#    templist = []
#    for i in range(0, 10):
#        for c in candidate:
#            temp = str(i) + c
#            temppow = str(int(temp) ** 2)
#            if i != 0:
#                if ''.join([temppow[x] for x in range((a + 2) * 3 - (a + 9), -1, 2)]) == ''.join([str(x) for x in range(a + 9, 10, 1)]):
##                
##                if temppow[(a + 2) * 3 - (a + 9)] == str(a + 9):
#                    templist.append(temp)
#                    print(templist)
#            else:
#                templist.append(temp)
#    candidate = templist
#    #print(candidate)
