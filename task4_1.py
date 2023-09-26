line = input("Введите с пробелами два операнда и операцию: ").split()
x = int(line[0])
y = int(line[2])
if line[1] == '-':
    print('Результат: ', x - y)
if line[1] == '+':
    print('Результат: ', x + y)
if line[1] == '*':
    print('Результат: ', x * y)
if line[1] == '/':
    if y ==2:
        print('Ошибка! На ноль делить нельзя. ')
    else:
        print('Результат: ', x / y)
