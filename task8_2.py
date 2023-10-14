
M = [[1, 555555, 3], [2, 44, 1, 4], [3, 33333333]]

for i in M:
    s = ''
    for j in i:
        s += str(j)
    i.append(len(s))

M = sorted(M, key=lambda x: x[-1])
for i in range(len(M)):
    M[i].pop(-1)
    M[i] = sorted(M[i], reverse=True)
print(M)
