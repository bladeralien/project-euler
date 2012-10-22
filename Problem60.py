import Primes
#mylist = [3, 7, 109, 673]

#for ap in Primes.primes[Primes.primes.index(673)+1:]:
#    print(ap)
#    booltemp = True
#    for a in mylist:
#        if Primes.isPrime(int(str(ap) + str(a))) == False or Primes.isPrime(int(str(a) + str(ap))) == False:
#            booltemp = False
#            break
#    if booltemp == True:
#        print(ap)
#        break
for ap in Primes.primes:
    print(ap)
    mylist = [[ap]]
    found = False
    while True:
        templist = []
        for a in mylist:
            for b in Primes.primes[Primes.primes.index(a[-1]) + 1:]:
                booltemp = True
                for i in a:
                    if Primes.isPrime(int(str(i) + str(b))) == False or Primes.isPrime(int(str(b) + str(i))) == False:
                        booltemp = False
                        break
                if booltemp == True:
                    templist.append(a + [b])
        mylist = templist
        if mylist == []:
            break
        print(len(mylist[0]))
        if len(mylist[0]) == 5:
            print(mylist)
            found = True
            break
    if found == True:
        break

