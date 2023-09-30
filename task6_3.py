alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

s = input('Введите строку: ')
let = ''
sim = ''
num = ''
for i in s:
    if i in alfabet and i not in let:
        let += i + ''
    elif i in numbers and i not in num:
        num += i + ''
    elif i not in sim and i not in alfabet and i not in numbers:
        sim += i + ''
print('Вывод:\n', let, '\n', num, '\n', sim)