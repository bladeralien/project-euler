#evens = set(['0', '2', '4', '6', '8'])
evens = ['0', '2', '4', '6', '8']
odds = ['1', '3', '5', '7', '9']
i, count = 1, 0
while i < 1000000000:
    if i % 100000 == 0:
        print(i)
    if i % 10 != 0:
        temp = str(i + int(str(i)[::-1]))
        temp = set(list(temp))
        if temp == odds:
            count += 1
#        reversible = True
#        for e in evens:
#            if e in temp:
#                reversible = False
#                break
#        if reversible == True:
#            count += 1
#        if len(set(list(str(temp))).intersection(evens)) == 0:
#            count += 1
#    ir = str(i)[::-1]
#    if ir.startswith('0') == False:
#        temp = i + int(ir)
#        if len(set(list(str(temp))).intersection(evens)) == 0:
#            count += 1
    i += 1
print(count)
