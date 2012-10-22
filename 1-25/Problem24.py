#Lucky.

import itertools

k = 0
for i in itertools.permutations(range(10)):
    k += 1
    if k == 1000000:
        print(i)
