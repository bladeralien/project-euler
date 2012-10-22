class Card:
    mapdict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    def __init__(self, astr):
        self.strrepr = astr
        self.value = Card.mapdict[astr[0]]
        self.suit = astr[1]
    def __str__(self):
        return self.strrepr
    def returnvalue(self):
        return self.value
    def returnsuit(self):
        return self.suit
    def __cmp__(self, other):
        if self.returnvalue() > other.returnvalue():
            return 1
        if self.returnvalue() > other.returnvalue():
            return 0
        if self.returnvalue() > other.returnvalue():
            return -1

class Hand:
    def __init__(self, cardlist):
        self.cards = [Card(ac) for ac in cardlist]
    def returncards(self):
        return self.cards
    def values(self):
        valuedict = {}
        for ac in self.returncards():
            valuedict.setdefault(ac.returnvalue(), 0)
            valuedict[ac.returnvalue()] += 1
        valuelist = sorted(valuedict.items(), key = lambda item: item[-1])
        if len(valuelist) == 3:
            if valuelist[-1][-1] == 3:
                valuelist = sorted(valuelist[:-1], key = lambda item: item[0]) + [valuelist[-1]]
            if valuelist[-1][-1] == 2:
                valuelist = [valuelist[0]] + sorted(valuelist[1:], key = lambda item: item[0])
        if len(valuelist) == 4:
            valuelist = sorted(valuelist[:-1], key = lambda item: item[0]) + [valuelist[-1]]
        if len(valuelist) == 5:
            valuelist = sorted(valuelist, key = lambda item: item[0])
        return valuelist
    def suits(self):
        suits = [ac.returnsuit() for ac in self.returncards()]
        return set(suits)
    def rank(self):
        valuelist = self.values()
        if valuelist[-1][-1] == 1:
            if len(self.suits()) == 1:
                if valuelist[-1][0] - valuelist[0][0] == 4:
                    if valuelist[0][0] == 10:
                        return 9
                    return 8
                return 5
            else:
                if valuelist[-1][0] - valuelist[0][0] == 4:
                    return 4
                else:
                    return 0
        if valuelist[-1][-1] == 2:
            if len(valuelist) == 3:
                return 2
            if len(valuelist) == 4:
                return 1
        if valuelist[-1][-1] == 3:
            if len(valuelist) == 2:
                return 6
            if len(valuelist) == 3:
                return 3
        if valuelist[-1][-1] == 4:
            return 7
    def __gt__(self, other):
        if self.rank() > other.rank():
            return True
        elif self.rank() < other.rank():
            return False
        else:
            svalue = self.values()
            ovalue = other.values()
            for i in range(len(svalue) - 1, -1, -1):
                if svalue[i][0] > ovalue[i][0]:
                    return True
                elif svalue[i][0] < ovalue[i][0]:
                    return False
                else:
                    pass
        return False
source = [line.strip().split(' ') for line in open('Problem54.txt').readlines()]
count = 0
for line in source:
    handa = Hand(line[:5])
    handb = Hand(line[5:])
    if handa > handb:
        count += 1
print(count)
