def F(s):
    s = s.split(',')
    M = []
    for i in s:
        c = i
        c = c.split('-')
        a, b = int(c[0]), int(c[1])
        for j in range(a, b + 1):
            M.append(j)
    return M


S = input('Введите строку диапазонов: ')
print(F(S))