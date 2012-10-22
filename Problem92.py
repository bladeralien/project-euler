count = 0
for i in range(1, 10000000):
    if i % 10000 == 0: print(i)
    chain = i
    while True:
        if chain == 1:
            break
        if chain == 89:
            count += 1
            break
        chain = sum(int(x) ** 2 for x in list(str(chain)))
print(count)
