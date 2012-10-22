def mylazyfunc():
    import itertools
    primes = [int(line.strip()) for line in open('Primes.txt').readlines()]
    primesset = set([int(line.strip()) for line in open('Primes.txt').readlines()])
    for ap in primes:
        print(ap)
        strap = str(ap)
        mydigits = {}
        if len(strap) != len(set(list(strap))):
            for i in range(len(strap)):
                mydigits.setdefault(strap[i], [])
                mydigits[strap[i]].append(i)
        for adigit in mydigits:
            if len(mydigits[adigit]) >= 2:
                for k in range(2, len(mydigits[adigit]) + 1):
                    for indexs in itertools.combinations(mydigits[adigit], k):
                        if 0 not in indexs:
                            tempcount = 0
                            for d in range(10):
                                temp = ''
                                for i in range(len(strap)):
                                    if i in indexs:
                                        temp += str(d)
                                    else:
                                        temp += strap[i]
                                if int(temp) in primesset:
                                    tempcount += 1
                            if tempcount == 8:
                                print(ap, indexs)
                                return ap
                        else:
                            tempcount = 0
                            for d in range(1, 10):
                                temp = ''
                                for i in range(len(strap)):
                                    if i in indexs:
                                        temp += str(d)
                                    else:
                                        temp += strap[i]
                                if int(temp) in primesset:
                                    tempcount += 1
                            if tempcount == 8:
                                print(ap, indexs)
                                return ap                            
print(mylazyfunc())



