n = int(input("Введите число: "))
M = [1]
for i in range(1,n + 1):
    c = 1
    for j in range(1, i + 1):
        print(c, sep=' ', end=' ')
        c = c * (i - j) // j
    print()