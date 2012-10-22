def factorial(n):
    """require n greater than or equal to one."""
    temp = 1
    for item in range(2, n+1):
        temp *= item
    return temp


def permutation(n, r):
    temp = 1
    for item in range(n - r + 1, n + 1):
        temp *= item
    return temp


def combination(n, r):
    return permutation(n, r) / factorial(r)


def bin(n):
    pass


class Fibs:

    def __init__(self):
        self.mylist = [1, 1]

    def __getitem__(self, k):
        if k > len(self.mylist):
            for i in range(k - len(self.mylist)):
                self.mylist.append(self.mylist[-2] + self.mylist[-1])
        return self.mylist[k - 1]
