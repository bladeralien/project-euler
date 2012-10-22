i = 1
while True:
    if i % 100 == 0:
        print(i)
    templist = [str(x) for x in [i * 1, i * 2, i * 3, i * 4, i * 5, i * 6]]
    tempset = set(list(''.join(templist)))
    if tempset == set(list(str(x))):
        print(i)
        break
    i += 1
