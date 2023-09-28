n = int(input("Введите число: "))
a = 0
b = 1
for i in range(n):
    a, b = b, a + b
    if i == (n - 1):
        print(a)
        break
    print(a, end=', ')