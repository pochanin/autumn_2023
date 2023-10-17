def gen():
    num = 1
    while True:
        yield num
        if num > 0:
            num = -num - 1
        else:
            num = -num + 1


gen_1 = gen()
for i in range(10):
    print(next(gen_1))
