st = input('Введите строку: ').lower()
sl = {}
for i in st:
    if i not in sl.keys():
        sl[i] = 1
    else:
        sl[i] += 1

sl = sorted(sl.items(), key=lambda x: (-x[1], x[0]))

for i, j in sl[:10]:
    print(i, '-', j)