logs = [line.strip() for line in open('Problem79.txt').readlines()]
relations = []
for alog in logs:
    relations.append(alog[:-1])
    relations.append(alog[1:])
    relations.append(alog[0] + alog[-1])
relations = list(set(relations))
relations.sort()
print(relations)
# to be continued.
