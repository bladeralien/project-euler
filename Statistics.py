import math


def median(data):
    values = sorted(data)
    if len(values) % 2 == 1:
        return values[(len(values) + 1) / 2 - 1]
    else:
        lower = values[len(values) / 2 - 1]
        upper = values[len(values) / 2]
        return (lower + upper) / 2


def percentile(percent, alist):
    sortedlist = sorted(alist)
    k = (len(sortedlist) - 1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sortedlist[int(k)]
    d0 = sortedlist[int(f)] * (k - f)
    d1 = sortedlist[int(c)] * (c - k)
    return d0 + d1


def mean(data):
    return sum(data) / len(data)


def variance(data):
    temp = 0
    meanofdata = mean(data)
    for value in data:
        temp += (value-meanofdata) ** 2
    if len(data) == 1:
        return None
    return temp / (len(data) - 1)


def RSD(data):
    meanofdata = mean(data)
    varianceofdata = variance(data)
    if meanofdata == 0 or varianceofdata == None:
        return None
    return abs(math.sqrt(varianceofdata) / meanofdata)
