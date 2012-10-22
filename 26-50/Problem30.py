for candidate in range(1, 1000000):
    if candidate == sum([int(x) ** 5 for x in list(str(candidate))]):
        print(candidate)
