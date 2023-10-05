import lamda

M = [[1, 5, 3], [2, 44, 1, 4], [3, 3]]
sorted_M = sorted(M, key=lambda x: len(x))
for i in sorted_M:
    i.sort()
    i.reverse()
print(sorted_M)
