from random import randint
def answer(N):
    numbers = []
    for i in N:
        for j in i:
            numbers.append(j)
    numbers.sort()
    return [numbers[-3], numbers[-2], numbers[-1]]

n = int(input('Введите n: '))
m = int(input('Введите m: '))
M = [[randint(1, 100) for i in range(m)] for j in range(n)]
print(M)
print(answer(M))