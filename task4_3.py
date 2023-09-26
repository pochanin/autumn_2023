alfabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзиклмнопрстуфхцчшщэюя'
f1 = input("Введите первое предложение: ").lower()
f2 = input("Введите второе предложение: ").lower()
M = []
N = []
for i in f1:
    if i in alfabet:
        M.append(i)

for i in f2:
    if i in alfabet:
        N.append(i)

if sorted(M) == sorted(N):
    print(True)
else:
    print(False)
