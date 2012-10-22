# The number of partitions of n into no more than k parts is the same as
# the number of partitions of n + k into exactly k parts.


memory = {}


def partitions_helper(n, k):
    if k == 1 or k == n:
        return 1
    if k > n:
        return 0
    if (n, k) in memory:
        return memory[(n, k)]
    count = 0
    for i in range(1, k + 1):
        count += partitions_helper(n - k, i)
    memory[(n, k)] = count
    return count


def partitions(n):
    count = 0
    for k in range(2, n + 1):
        print k
        count += partitions_helper(n, k)
    return count


print(partitions(100))
