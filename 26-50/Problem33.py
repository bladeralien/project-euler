for a in range(10, 100):
    for b in range(a + 1, 100):
        if list(str(a))[1] == list(str(b))[0]:
            if b % 10 != 0 and float(a) / b == float(a / 10) / (b % 10):
                print(a, b)
