def gen():
    num = 1
    while True:
        num_str = str(num)
        if num_str ==num_str[::-1]:
            yield num
        num += 1


gen_1 = gen()
for i in range(20):
    print(next(gen_1), end=' ')
