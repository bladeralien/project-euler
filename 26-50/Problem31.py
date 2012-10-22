def mapdenomination(d):
    mydict = {1: 'A', 2: 'B', 5: 'C', 10: 'D', 20: 'E', 50: 'F', 100: 'G', 200: 'H'}
    return mydict[d]


def currencycombinations(currency, memory):
    denominations = [1, 2, 5, 10, 20, 50, 100, 200]
    if currency == 0:
        return ['']
    if currency == 1:
        return ['A']
    if currency in memory:
        return memory[currency]
    #print('call ' + str(currency))
    combinations = []
    for d in denominations:
        if currency - d >= 0:
            templist = currencycombinations(currency - d, memory)
            memory[currency - d] = templist
            for combination in templist:
                combinations.append(mapdenomination(d) + combination)
    combinations = list(set([''.join(sorted(list(combination))) for combination in combinations]))
    memory[currency] = combinations
    #print('leave ' + str(currency))
    return combinations
print(len(currencycombinations(200, {})))
