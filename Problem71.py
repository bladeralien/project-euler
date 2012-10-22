# The easy way.
# 3 / 7 = (3 * 142857) / (7 * 142857) = 428571 / 999999
# The hard way.
import math
immediatelyn, immediatelyd, immediately = 2, 5, float(2)/5
for d in range(2, 1000001):
    print(d)
    for n in range(int(float(d)*immediatelyn/immediatelyd)+1, int(math.ceil(float(d)*3/7))):
        if float(n)/d > immediately:
            immediatelyn, immediatelyd, immediately = n, d, float(n)/d
print([immediatelyn, immediatelyd])
