Fib_N_1, Fib_N_2, N_1 = 1, 1, 2
while True:
    Fib_N_1, Fib_N_2, N_1 = Fib_N_1 + Fib_N_2, Fib_N_1, N_1 + 1
    if len(str(Fib_N_1)) == 1000:
        print(N_1)
        break
