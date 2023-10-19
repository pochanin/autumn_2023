def F(n):
    if n < 10:
        return 1
    else:
        return 1 + F(n // 10)

a = int(input('Введите число: '))
print('Количество цифр:', F(a))