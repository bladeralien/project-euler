mynumbers = open('Problem13.txt').readlines()
allsum = 0
##SolutionA
allsum = sum([int(x.strip()) for x in mynumbers])
##SolutionB
##for i in range(100):
##    mynumbers[i] = [int(x) for x in list(mynumbers[i].strip())]
##for i in range(50):
##    asumd = 0
##    for k in range(100):
##        asumd += mynumbers[k][i]
##    allsum += asumd * 10 ** (49 - i)
print(allsum)
