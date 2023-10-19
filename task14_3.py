def F(n):
    if n > 0:
        print('*' * n)
        F(n - 1)
        if n > 1:
            print('*' * n)


a = int(input('Введите число: '))
F(a)