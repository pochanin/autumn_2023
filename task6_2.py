s1 = input('Введите список книг ученика 1: ').split(', ')
s2 = input('Введите список книг ученика 2: ').split(', ')
count = 0
for i in s1:
    if i in s2:
        count += 1
print('Ответ: ', count)