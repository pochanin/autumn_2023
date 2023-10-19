def F(n):
    if n < 10:
        return n
    else:
        return n % 10 + F(n // 10)

a = int(input('Введите число: '))
print('Сумма цифр:', F(a))
