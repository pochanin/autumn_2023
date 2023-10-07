alfabet = 'ауоыиэяюёе'
x = input('Введите слово для поиска ему похожих: ')
n = int(input('Введите количество слов для сравнения: '))
M = []
answer = []
for i in range(n):
    word = input('Введите слово' + str(i + 1) + ': ')
    M.append(word)

let = []
for i in range(len(x)):
    if x[i] in alfabet:
        let.append(i)

for word in M:
    count_1 = count_2 = 0
    for i in range(len(word)):
        if word[i] in alfabet:
            count_1 += 1
    if count_1 ==len(let) and len(word) >= let[-1]:
        for i in range(len(word)):
            if word[i] in alfabet and i in let:
                count_2 += 1
        if count_1 == count_2:
            answer.append(word)

print(*answer)

