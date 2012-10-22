asum, sumsquare = 0, 0
for i in range(100):
    sumsquare += (i + 1) * (i + 1)
    asum += (i + 1)
print(asum * asum - sumsquare)
