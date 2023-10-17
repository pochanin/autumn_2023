def gen(m):
    for i in m:
        if i % 2 != 0:
            yield i


M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
gen_1 = gen(M)
for i in gen_1:
    print(i, end=' ')
