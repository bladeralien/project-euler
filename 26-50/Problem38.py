for i in range(1000, 10000):
    concatenated = str(i) + str(i * 2)
    if len(concatenated) == 9 and len(set(list(concatenated))) == 9 and '0' not in concatenated:
        print(str(i) + ' * (1, 2) = ' + concatenated)

for i in range(100, 1000):
    concatenated = str(i) + str(i * 2) + str(i * 3)
    if len(concatenated) == 9 and len(set(list(concatenated))) == 9 and '0' not in concatenated:
        print(str(i) + ' * (1, 2, 3) = ' + concatenated)

for i in range(10, 100):
    concatenated = str(i) + str(i * 2) + str(i * 3) + str(i * 4)
    if len(concatenated) == 9 and len(set(list(concatenated))) == 9 and '0' not in concatenated:
        print(str(i) + ' * (1, 2, 3, 4) = ' + concatenated)

print('9 * (1, 2, 3, 4, 5) = 918273645')
print('1 * (1, 2, 3, 4, 5, 6, 7, 8, 9) = 123456789')
