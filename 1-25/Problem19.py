days = [31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['M', 'T', 'W', 'Th', 'F', 'S', 'Su']

def daysoffeb(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 29
            return 28
        return 29
    return 28

templist = ['M']
for year in range(1900, 2001):
    for month in range(1, 13):
        if month == 2:
            templist.append(weeks[(weeks.index(templist[-1]) + daysoffeb(year) % 7) % 7])
        else:
            templist.append(weeks[(weeks.index(templist[-1]) + days[month - 1] % 7) % 7])
print(templist[12:-1].count('Su'))
